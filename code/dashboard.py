import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import geopandas as gpd
import streamlit_folium as stf
import folium

# Load in datasets:
acled_final = pd.read_csv("cache/acled_final.csv")
displacement_final = pd.read_csv("cache/displacement_final.csv")
displacement_melt = pd.read_csv("cache/displacement_melt.csv")

st.title("Final Project: IST 356")
st.markdown('''
This project visualizing the ongoing conditions of the war in Sudan,
displaying the rampant violence towards civilians throughout the country
and how that impacts internal displacement.
''')

# Create Map with Folium and Geopandas:
st.markdown("## ACLED Violence Toward Civilians Data")
## Get selections for state:
toggle_state = st.toggle("Toggle Filtering by State")
if toggle_state:
    state_list = displacement_final["State"].unique()
    select_state = st.selectbox("Select State:", state_list)
## Get selections from different types of political violence:
toggle_type = st.toggle("Toggle Filtering by Type")
if toggle_type:
    acled_select_list = acled_final["sub_event_type"].unique()
    select_type = st.selectbox("Select Event Type:", acled_select_list)

## Creating map:
baseMap = folium.Map(location = (15.5974, 32.5356), zoom_start = 6) # coordinates for Khartoum
geo_df = gpd.GeoDataFrame(acled_final, geometry=gpd.points_from_xy(acled_final['longitude'], acled_final['latitude']))
if toggle_type and select_type:
    geo_df = geo_df[geo_df["sub_event_type"] == select_type]

if toggle_state and select_state:
    geo_df = geo_df[geo_df["admin1"] == select_state]

final_geom = geo_df.explore(popup="actor1",lat = "latitude", lon ="longitude", m = baseMap, marker_type="marker", color = "actor1")
stf.folium_static(final_geom)

# Show Overview of Displacement:
st.markdown("## Internally Displaced Peoples (IDPs)")
fig1, ax1 = plt.subplots()
fig1.suptitle("Internally Displaced People (IDPs) by State")
sns.barplot(data = displacement_final, x = "State", y = "IDPs", ax = ax1)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig1)

# Showing Statistics on Selected State:
if toggle_state and select_state:
    displacement_melt = displacement_melt[displacement_melt["State"] == select_state]
    st.markdown("### State Statistics")
    col1, col2 = st.columns(2)
    fig2, ax2 = plt.subplots()
    fig2.suptitle("Origins of Internally Displaced Population")
    sns.barplot(data = displacement_melt, x = "Origin_State", y = "IDPs_Origin", ax = ax2)
    plt.xticks(rotation=45, ha='right')
    col1.pyplot(fig2)

    totalIDPs = displacement_final["IDPs"].sum()
    col2.write(f"Total IDPs: {totalIDPs}")
    stateIDPs = displacement_final[displacement_final["State"] == select_state]["IDPs"].sum()
    col2.write(f"Total State IDPs: {stateIDPs}")
    percentTotalIDP = round((stateIDPs/totalIDPs) * 100, 3)
    col2.metric("Percent of IDPs from Total:", value = f"{percentTotalIDP} %")

# Leaving sources and attributions:
st.markdown("### Data Sources")
st.markdown("""
- [Armed Conflict Location & Event Data Project (ACLED)](https://acleddata.com/)
- [International Organization for Migration - Displacement Tracking Matrix (IOM DTM)](https://dtm.iom.int/sudan)
- [Humanitarian Data Exchange (HDX)](https://data.humdata.org/)
""")







