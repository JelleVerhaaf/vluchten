import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
url_csv = 
df = pd.read_csv(url_csv, sep = ';', decimal = ',')

vliegvelden_comp = df.copy()
vliegvelden_comp = vliegvelden_comp[['ICAO', 'Longitude', 'Latitude']]
vliegvelden_comp

vluchten_loc = vluchten.copy()
vluchten_loc = vluchten_loc['Org/Des']

locaties = vliegvelden_comp.merge(vluchten_loc, left_on = 'ICAO', right_on = 'Org/Des')

locaties = locaties.dropna()

locaties = locaties.drop_duplicates(subset = 'Org/Des')



# Streamlit dropdown for continent selection
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
selected_continent = st.selectbox("Select a Continent", continents)


# Initialize Folium map centered on the selected continent's coordinates
continent_centers = {
    "Africa": [0, 20],
    "Asia": [34, 100],
    "Europe": [54, 15],
    "North America": [40, -100],
    "South America": [-15, -60],
    "Oceania": [-25, 140]
}

# Create Folium map centered on the continent and set to fixed zoom level
map_center = continent_centers[selected_continent]
m = folium.Map(location=map_center, zoom_start=3, max_bounds=True, dragging=False, scrollWheelZoom=False)

# Adding markers for each airport
for idx, row in locaties.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Org/Des']}",  # Show airport code on click
        icon=folium.Icon(color='blue')
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)
