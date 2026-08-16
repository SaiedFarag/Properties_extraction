# Properties Extraction

Extracts a defined set of land parcels from a large statewide dataset using Public Land
Survey System (PLSS) descriptions — Township, Range and Section numbers.

## The problem

Land holdings in much of the United States are described in PLSS terms rather than by
coordinates or parcel ID. A target area might be specified as *"Township 19, Range 35,
Sections 2, 4, 5, 8, 9, 11"* and so on, across dozens of township/range combinations.

Selecting those parcels by hand from a dataset covering an entire state is slow and
error-prone. This script encodes the full list of PLSS descriptions and pulls the matching
parcels out in one pass, then reports how many duplicate records the combined selection
produced — duplicates are expected where selections overlap, and the count is a check that
the description list was transcribed correctly.

## Requirements

```bash
pip install -r requirements.txt
```

- Python 3.8+
- `geopandas`, `pandas`

## Usage

Place the source parcel dataset in the repository root as `Township_template.shp` (with
its sidecar files), then:

```bash
python extract_properties.py
```

The dataset must have integer `Township`, `Range` and `Section` columns alongside its
geometry.

The script prints the number of duplicate records found across the combined selection.
The export step at the end is commented out — uncomment it to write the result:

```python
appended_gdf.to_file('extracted_parcels.shp')
```

## Adapting it to a different area

The selection is expressed as 77 blocks, one per township/range pair:

```python
condition9 = parcels_data[(parcels_data['Township'] == 19) & (parcels_data['Range'] == 34)]
section9 = condition9[condition9['Section'].isin([5, 6, 24, 25, 31])]
```

To target a different area, replace these blocks with your own township/range/section
list and update `gdf_list` at the bottom to match.

## Known issues in the current selection list

Two values in the hardcoded list look like transcription errors and are marked with
`NOTE:` comments in the source:

| Line | Value | Problem |
|------|-------|---------|
| ~93 | `Section 335` | Section numbers run 1–36, so this matches nothing |
| ~98 | `Range 3` | Every other range is between 28 and 39; likely truncated |

Neither causes a crash — both simply select no parcels — so they would go unnoticed
without checking the output count. They need verifying against the original source
description before the results are relied on.
