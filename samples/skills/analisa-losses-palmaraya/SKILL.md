---
name: analisa-losses-palmaraya
description: Gunakan saat saya meminta analisa losses, rendemen, mutu hancak, atau pemupukan di workbook Palmaraya. Gunakan juga saat saya minta dibuatkan dashboard, ringkasan KPI, tabel pivot, atau grafik dari data produksi kelapa sawit.
---

# Cara membangun analisa losses dan rendemen Palmaraya

Analisa yang baik menjawab satu pertanyaan: ke mana minyaknya pergi, dan siapa yang
harus berbuat apa. Analisa yang buruk hanya menampilkan angka dan menyerahkan
kesimpulan kepada pembaca. Bangun jenis yang pertama, selalu.

## Jangan pernah menimpa data mentah

Semua hasil ditulis di sheet baru. Sheet sumber tidak boleh diubah, difilter permanen,
diurutkan ulang, atau dihapus kolomnya. Beri nama sheet baru dengan awalan
`Analisa_`, `Dashboard_`, atau `Ringkasan_`.

## Standar yang berlaku, jangan dikarang

Gunakan angka standar berikut. Jangan memakai standar lain kecuali saya menyebutkannya.

| Ukuran | Standar Palmaraya |
| --- | --- |
| Rendemen minyak (OER) | 23,2 persen terhadap TBS olah |
| Rendemen inti (KER) | 5,1 persen terhadap TBS olah |
| Losses tandan kosong | maksimal 0,45 persen |
| Losses unstripped bunch | maksimal 0,10 persen |
| Losses ampas press | maksimal 0,60 persen |
| Losses biji | maksimal 0,20 persen |
| Losses sludge dan final effluent | maksimal 0,55 persen |
| Brondolan tidak terkutip | maksimal 2,0 butir per pokok |
| Restan janjang | maksimal 24 jam |
| Rasio hancak | 12 hektar per pemanen |
| Kalium daun | nilai kritis 1,00 persen |
| Losses panen total | maksimal 1,5 persen terhadap produksi |

Sheet `Standar_Losses`, `Parameter_Penilaian`, dan `Standar_Kritis_Hara` di dalam workbook
adalah rujukan resmi. Baca dari sana bila tersedia, jangan mengetik ulang dari ingatan.

## Setiap selisih diterjemahkan ke rupiah

Angka persen tidak menggerakkan siapa pun. Selalu tambahkan kolom nilai rupiah:

- Selisih OER terhadap target dikalikan TBS olah dikalikan harga CPO bulan berjalan.
- Losses panen dalam kilogram dikalikan 0,22 lalu dikalikan harga CPO.
- Gunakan sheet `Harga_CPO` untuk harga bulan yang sesuai, bukan satu harga rata-rata.

Tulis rupiah dengan format `#,##0` tanpa desimal.

## Struktur dashboard

Bangun dalam urutan ini di satu sheet `Dashboard`:

1. Empat kartu KPI di baris atas: rendemen berjalan, selisih terhadap target dalam poin
   persentase, nilai selisih dalam rupiah setahun, dan unit dengan kinerja terburuk.
2. Satu grafik garis: tren bulanan indikator utama, dengan garis target sebagai pembanding.
3. Satu grafik batang: peringkat unit dari terburuk ke terbaik, bukan urutan abjad.
4. Satu grafik kolom bertumpuk: komposisi penyebab, misalnya losses per stasiun.
5. Satu tabel ringkas maksimal 10 baris berisi unit yang melewati ambang, dengan kolom
   status dan tindakan yang disarankan.

Semua grafik dibuat asli di Excel, bukan gambar tempelan. Beri label data. Beri satu
kalimat keterangan di bawah setiap grafik yang menyatakan temuannya.

## Peringkat selalu dari yang terburuk

Saat menampilkan unit, PKS, estate, afdeling, mandor, atau blok, urutkan dari kinerja
terburuk. Yang perlu ditindak harus muncul di baris pertama, bukan di baris terakhir.

## Turunkan sampai ke tingkat yang bisa ditindak

Berhenti di tingkat grup berarti tidak ada yang bisa dikerjakan besok pagi. Selalu turun
sampai satu tingkat di bawah temuan: dari grup ke PKS, dari PKS ke stasiun, dari estate
ke afdeling, dari afdeling ke mandor dan blok. Sebutkan nama unit, nama mandor, dan kode
blok secara eksplisit.

## Uji hubungan, bukan hanya menampilkan angka

Bila saya menanyakan penyebab, bandingkan minimal dua kelompok dan sebutkan selisihnya:
masa kerja pemanen di bawah 6 bulan terhadap di atas 12 bulan, blok dengan kalium di
bawah kritis terhadap yang di atas kritis, bulan basah terhadap bulan kering, mandor
terhadap mandor. Sebutkan besar selisihnya dalam angka.

## Bila data tidak ada

Jangan mengarang angka dan jangan meninggalkan sel kosong tanpa penjelasan. Tulis di sel
atau di catatan analisa: kolom apa yang dibutuhkan, di sheet mana seharusnya berada, dan
bagian analisa mana yang tidak dapat diselesaikan karenanya.

## Sebelum selesai, periksa

- Sheet sumber tidak berubah sama sekali.
- Setiap grafik punya label data dan satu kalimat keterangan temuan.
- Setiap selisih persen sudah punya pasangan nilai rupiahnya.
- Peringkat dimulai dari yang terburuk.
- Setiap temuan menyebut unit, orang, atau blok yang spesifik.
- Angka yang ditulis di ringkasan sama persis dengan angka di tabel pendukungnya.
