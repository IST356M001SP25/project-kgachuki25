# Preparing and transforming the data from extract
# to be used in the visualizations.
import pandas as pd

# ACLED Data Preparation:
acled_df = pd.read_csv("cache/acled_data.csv")

## Filtering needed Columns:
cols_acled = ["event_id_cnty", "sub_event_type", "admin1", "actor1", "latitude", "longitude", "fatalities"]
acled_df2 = acled_df[cols_acled]

# Importing HumData Excel Sheet and Cleaning:
## First 4 rows and 6th row not needed, colnames in 4th
displacement_df = pd.read_excel("cache/DTM Sudan IDPs Master List Round 7.xlsx",
                                sheet_name = 1, header = 4, skiprows = [5])

## Removing whitespace around column names
displacement_df.columns = displacement_df.columns.str.strip()

## Filtering and changing column names
filtercols2 = ["STATE CODE", "HHs", "SUDANESE", "NON SUDANESE"]
displacement_df = displacement_df.drop(columns = filtercols2)
displacement_df = displacement_df.replace("Aj Jazirah", "Al Jazirah")
displacement_df = displacement_df.rename(columns = {"Aj Jazirah":"Al Jazirah", "STATE OF DISPLACEMET":"State"})

## Making melted table for later visuals:
displacement_melt = displacement_df.melt(id_vars=["State", "IDPs"], var_name="Origin_State", value_name="IDPs_Origin")

# Exporting data for visualizaton:
acled_df2.to_csv("cache/acled_final.csv", index = False)
displacement_df.to_csv("cache/displacement_final.csv", index = False)
displacement_melt.to_csv("cache/displacement_melt.csv", index = False)