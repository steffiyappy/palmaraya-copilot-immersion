# -*- coding: utf-8 -*-
# =============================================================================
# PALMARAYA · PEMUAT DATA MICROSOFT FABRIC
# Salin SELURUH isi berkas ini ke SATU cell notebook, lalu klik Run.
# Tidak perlu mengunggah berkas apa pun. Data diambil langsung dari internet.
# Waktu jalan sekitar 2 sampai 4 menit.
# =============================================================================
#
# CARA PAKAI
#   1. Di workspace Fabric, buat Lakehouse baru (nama bebas, misalnya LH_Palmaraya).
#   2. Buat Notebook baru, lalu hubungkan ke lakehouse tersebut lewat tombol
#      Add data sources di panel kiri.
#   3. Tempel seluruh isi berkas ini ke satu cell, lalu Run all.
#   4. Selesai. 19 tabel dan 4 view siap dipakai.
#
# JIKA WORKSPACE ANDA MEMBLOKIR AKSES INTERNET
#   Ubah SUMBER menjadi "lokal" di bawah, lalu unggah folder samples/csv
#   ke Files/palmaraya/ pada lakehouse Anda terlebih dahulu.
# =============================================================================

SUMBER = "internet"   # "internet" (tanpa unggah) atau "lokal" (sudah diunggah manual)
URL_DASAR = "https://raw.githubusercontent.com/steffiyappy/palmaraya-copilot-immersion/main/samples/csv"
FOLDER_LOKAL = "Files/palmaraya"

TABEL = [
    "Master_Blok", "Master_Pemanen", "Panen_Harian_Afdeling", "Losses_Panen_Blok",
    "Inspeksi_Mutu_Hancak", "Losses_Sampel_PKS", "Produksi_Harian_PKS",
    "Sortasi_TBS_Loading_Ramp", "Downtime_PKS", "Analisa_Daun_LSU", "Analisa_Tanah",
    "Rekomendasi_Pupuk", "Realisasi_Aplikasi_Pupuk", "Produksi_Blok_Bulanan",
    "Curah_Hujan_Harian", "Harga_CPO_Bulanan", "Standar_Losses_PKS",
    "Parameter_Mutu_Hancak", "Standar_Kritis_Hara",
]
KOLOM_TANGGAL = ["Tanggal", "TanggalSampling", "TanggalMasuk"]

import pandas as pd
from pyspark.sql.functions import col, to_date

print(f"Memuat {len(TABEL)} tabel Palmaraya · sumber: {SUMBER}\n")
berhasil, gagal = [], []

for i, nama in enumerate(TABEL, 1):
    try:
        if SUMBER == "internet":
            # dibaca dengan pandas agar tidak perlu unggah apa pun ke lakehouse
            pdf = pd.read_csv(f"{URL_DASAR}/{nama}.csv")
            df = spark.createDataFrame(pdf)
        else:
            df = (spark.read.option("header", True).option("inferSchema", True)
                  .csv(f"{FOLDER_LOKAL}/{nama}.csv"))

        for k in KOLOM_TANGGAL:
            if k in df.columns:
                df = df.withColumn(k, to_date(col(k)))

        df.write.mode("overwrite").option("overwriteSchema", "true") \
          .format("delta").saveAsTable(nama)
        n = df.count()
        berhasil.append(nama)
        print(f"  [{i:2d}/{len(TABEL)}] {nama:30s} {n:>7,} baris")
    except Exception as e:
        gagal.append((nama, str(e)[:120]))
        print(f"  [{i:2d}/{len(TABEL)}] {nama:30s} GAGAL: {str(e)[:120]}")

print(f"\nTabel berhasil dimuat: {len(berhasil)} dari {len(TABEL)}")
if gagal:
    print("Tabel gagal:")
    for nama, pesan in gagal:
        print(f"  - {nama}: {pesan}")
    print("\nJika seluruhnya gagal, kemungkinan workspace memblokir akses internet.")
    print('Ubah SUMBER menjadi "lokal", unggah folder samples/csv ke Files/palmaraya/, lalu jalankan ulang.')

# =============================================================================
# VIEW RINGKASAN · mempermudah pertanyaan bahasa biasa lewat Fabric data agent
# =============================================================================
if len(berhasil) >= 15:
    spark.sql("""
    CREATE OR REPLACE VIEW VwRendemenBulanan AS
    SELECT  PKS, Wilayah, Bulan, NamaBulan,
            ROUND(SUM(TBS_Olah_Ton), 1)                             AS TBS_Olah_Ton,
            ROUND(SUM(CPO_Ton), 1)                                  AS CPO_Ton,
            ROUND(SUM(CPO_Ton) / SUM(TBS_Olah_Ton) * 100, 2)        AS OER_Persen,
            23.2                                                    AS TargetOER_Persen,
            ROUND(SUM(CPO_Ton) / SUM(TBS_Olah_Ton) * 100 - 23.2, 2) AS GapOER_pp,
            ROUND(SUM(Downtime_Jam), 1)                             AS Downtime_Jam
    FROM    Produksi_Harian_PKS
    GROUP BY PKS, Wilayah, Bulan, NamaBulan
    """)

    spark.sql("""
    CREATE OR REPLACE VIEW VwLossesStasiunBulanan AS
    SELECT  PKS, Stasiun, JenisLosses, Bulan, NamaBulan,
            ROUND(AVG(HasilAnalisa_Persen), 3)                           AS RataLosses_Persen,
            MAX(StandarMaks_Persen)                                      AS StandarMaks_Persen,
            ROUND(AVG(HasilAnalisa_Persen) - MAX(StandarMaks_Persen), 3) AS Deviasi_Persen,
            SUM(CASE WHEN Status = 'Melebihi Standar' THEN 1 ELSE 0 END) AS SampelDiAtasStandar,
            COUNT(*)                                                     AS JumlahSampel
    FROM    Losses_Sampel_PKS
    GROUP BY PKS, Stasiun, JenisLosses, Bulan, NamaBulan
    """)

    spark.sql("""
    CREATE OR REPLACE VIEW VwMutuHancakBulanan AS
    SELECT  Estate, Afdeling, Mandor, KelompokMasaKerja, Bulan, NamaBulan,
            ROUND(AVG(SkorTotal), 1)                            AS SkorRata2,
            SUM(CASE WHEN Grade IN ('C','D') THEN 1 ELSE 0 END) AS JumlahGradeCD,
            COUNT(*)                                            AS JumlahInspeksi,
            SUM(Denda_Rp)                                       AS TotalDenda_Rp
    FROM    Inspeksi_Mutu_Hancak
    GROUP BY Estate, Afdeling, Mandor, KelompokMasaKerja, Bulan, NamaBulan
    """)

    spark.sql("""
    CREATE OR REPLACE VIEW VwLossesPanenBulanan AS
    SELECT  Estate, Afdeling, Bulan, NamaBulan,
            ROUND(AVG(Brondolan_ButirPerPokok), 2)       AS Brondolan_ButirPerPokok,
            2.0                                          AS StandarBrondolan,
            ROUND(AVG(Losses_PersenTerhadapProduksi), 2) AS Losses_Persen,
            SUM(EstimasiKerugian_Rp)                     AS Kerugian_Rp,
            COUNT(*)                                     AS JumlahInspeksi
    FROM    Losses_Panen_Blok
    GROUP BY Estate, Afdeling, Bulan, NamaBulan
    """)

    print("\nView siap: VwRendemenBulanan · VwLossesStasiunBulanan · "
          "VwMutuHancakBulanan · VwLossesPanenBulanan")
    print("\nUji cepat, rendemen grup per bulan:")
    spark.sql("""
        SELECT Bulan, NamaBulan,
               ROUND(SUM(CPO_Ton)/SUM(TBS_Olah_Ton)*100, 2) AS OER_Persen
        FROM Produksi_Harian_PKS GROUP BY Bulan, NamaBulan ORDER BY Bulan
    """).show()
    print("Jika kolom OER_Persen menurun dari sekitar 22,77 ke 21,18, data Anda sudah benar.")
    print("\nLangkah berikutnya: buat Fabric data agent di atas lakehouse ini,")
    print("pilih seluruh tabel dan view, lalu terbitkan agar bisa ditanya dari Microsoft 365 Copilot.")
else:
    print("\nView tidak dibuat karena sebagian tabel gagal dimuat. Perbaiki dulu tabelnya.")
