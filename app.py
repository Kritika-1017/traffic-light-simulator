import streamlit as st
import folium
from streamlit_folium import st_folium

# Set page configuration
st.set_page_config(page_title="Chandigarh Traffic Light Simulation", layout="wide")

# Dummy junction data
junctions = [
    {
        "name": "Junction 1 - Sector 42",
        "location": [30.7170, 76.7380],
        "vehicles": {'A': 15, 'B': 0, 'C': 20, 'D': 10}
    },
    {
        "name": "Junction 2 - Sector 43",
        "location": [30.7260, 76.7650],
        "vehicles": {'A': 10, 'B': 0, 'C': 30, 'D': 25}
    },
    {
        "name": "Junction 3 - Sector 35",
        "location": [30.7352, 76.7732],
        "vehicles": {'A': 5, 'B': 2, 'C': 1, 'D': 4}
    },
]

# Title
st.title("🚦 Dynamic Traffic Light Simulation on Chandigarh Map")

# Mode
mode = st.radio("Select simulation mode:", ("Step-by-step", "Show all junctions"))

# Function to determine green light order
def get_green_order(vehicle_data):
    # Exclude 0 counts for fairness
    filtered = {k: v for k, v in vehicle_data.items() if v > 0}
    return sorted(filtered, key=filtered.get)

# Step-by-step mode
if mode == "Step-by-step":
    index = st.slider("Select junction:", 0, len(junctions) - 1)
    junction = junctions[index]

    st.subheader(junction["name"])
    m = folium.Map(location=junction["location"], zoom_start=16)
    folium.Marker(junction["location"], popup="Traffic Junction", icon=folium.Icon(color="red")).add_to(m)

    st.markdown(f"**Vehicle counts:** {junction['vehicles']}")
    green_order = get_green_order(junction["vehicles"])
    st.markdown(f"✅ **Green light order:** {', '.join(green_order)}")

    st_folium(m, width=700, height=500)

# Show all at once
else:
    m = folium.Map(location=[30.7333, 76.7794], zoom_start=13)
    for junc in junctions:
        folium.Marker(junc["location"], popup=junc["name"], icon=folium.Icon(color="red")).add_to(m)
    st_folium(m, width=900, height=500)

    for junc in junctions:
        st.subheader(junc["name"])
        st.markdown(f"**Vehicle counts:** {junc['vehicles']}")
        green_order = get_green_order(junc["vehicles"])
        st.markdown(f"✅ **Green light order:** {', '.join(green_order)}")
