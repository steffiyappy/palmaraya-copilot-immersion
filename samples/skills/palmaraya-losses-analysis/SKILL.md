---
name: palmaraya-losses-analysis
description: Use when I ask for analysis of losses, extraction rate, harvest quality, or fertiliser application in a Palmaraya workbook. Also use when I ask for a dashboard, a KPI summary, a pivot table, or charts built from palm oil production data.
---

# How to build a Palmaraya losses and extraction rate analysis

A good analysis answers one question: where did the oil go, and who has to do what
about it. A poor one displays numbers and leaves the reader to draw the conclusion.
Always build the first kind.

## Never overwrite the raw data

Write every result to a new sheet. Source sheets must not be edited, permanently
filtered, re-sorted, or have columns removed. Name new sheets with the prefix
`Analisa_`, `Dashboard_`, or `Ringkasan_`.

## Use the standards that apply, do not invent them

Use the figures below. Do not substitute other standards unless I give them to you.

| Measure | Palmaraya standard |
| --- | --- |
| Oil extraction rate (OER) | 23.2 percent of FFB processed |
| Kernel extraction rate (KER) | 5.1 percent of FFB processed |
| Empty fruit bunch losses | maximum 0.45 percent |
| Unstripped bunch losses | maximum 0.10 percent |
| Press fibre losses | maximum 0.60 percent |
| Nut and kernel losses | maximum 0.20 percent |
| Sludge and final effluent losses | maximum 0.55 percent |
| Uncollected loose fruit | maximum 2.0 per palm |
| Unevacuated bunches | maximum 24 hours |
| Harvester-to-area ratio | 12 hectares per harvester |
| Leaf potassium | critical value 1.00 percent |
| Total harvest losses | maximum 1.5 percent of production |

The `Standar_Losses`, `Parameter_Penilaian`, and `Standar_Kritis_Hara` sheets inside the
workbook are the authoritative reference. Read from them when they exist rather than
typing figures from memory.

## Translate every gap into rupiah

Percentages do not move anyone to act. Always add a rupiah value column:

- OER gap against target, multiplied by FFB processed, multiplied by that month's CPO price.
- Harvest losses in kilograms, multiplied by 0.22, multiplied by the CPO price.
- Use the `Harga_CPO` sheet for the price of the matching month, not a single average price.

Format rupiah as `#,##0` with no decimals.

## Dashboard structure

Build in this order on a single `Dashboard` sheet:

1. Four KPI cards along the top row: current extraction rate, gap against target in
   percentage points, the annual value of that gap in rupiah, and the worst-performing unit.
2. One line chart: the monthly trend of the main indicator, with the target as a reference line.
3. One bar chart: units ranked worst to best, not alphabetically.
4. One stacked column chart: the composition of the cause, for example losses by station.
5. One compact table of at most 10 rows listing units past the threshold, with a status
   column and a recommended action.

Build every chart natively in Excel, never as a pasted image. Add data labels. Put one
caption line under each chart stating what it shows.

## Always rank worst first

When listing units, mills, estates, divisions, foremen, or blocks, order them from worst
performance. Whatever needs acting on belongs in the first row, not the last.

## Drill down to a level someone can act on

Stopping at group level means nobody can do anything on Monday morning. Always go one
level below the finding: group to mill, mill to station, estate to division, division to
foreman and block. Name the unit, the foreman, and the block code explicitly.

## Test relationships, do not just display figures

When I ask about a cause, compare at least two groups and state the difference: harvesters
with under 6 months tenure against those over 12 months, blocks with potassium below the
critical value against those above it, wet months against dry months, foreman against
foreman. Give the size of the difference as a number.

## When the data is missing

Do not invent figures and do not leave blank cells without explanation. Write in the cell
or in the analysis notes: which column is needed, which sheet it should sit in, and which
part of the analysis cannot be completed as a result.

## Before you finish, check

- The source sheets are completely unchanged.
- Every chart has data labels and a one-line caption stating the finding.
- Every percentage gap has its matching rupiah value.
- Rankings start with the worst.
- Every finding names a specific unit, person, or block.
- The figures in the summary match the figures in the supporting tables exactly.
