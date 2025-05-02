
import streamlit as st
import folium
from streamlit_folium import st_folium
import time
import random

st.set_page_config(page_title="Chandigarh Traffic Light Simulation", layout="wide")

st.title("🚦 Dynamic Traffic Light Simulation on Chandigarh Map")

# Dummy vehicle data for each junction (4 sides: A, B, C, D)
junctions = [
    {"name": "Junction 1 - Sector 42", "location": [30.7135, 76.7224], "vehicles": {"A": 50, "B": 20, "C": 2, "D": 80}},
    {"name": "Junction 2 - Sector 38", "location": [30.7270, 76.7481], "vehicles": {"A": 15, "B": 0, "C": 30, "D": 5}},
    {"name": "Junction 3 - Sector 34", "location": [30.7353, 76.7734], "vehicles": {"A": 0, "B": 10, "C": 40, "D": 12}},
    {"name": "Junction 4 - Sector 26", "location": [30.7440, 76.7891], "vehicles": {"A": 5, "B": 0, "C": 0, "D": 25}},
    {"name": "Junction 5 - Sector 21", "location": [30.7520, 76.8004], "vehicles": {"A": 18, "B": 33, "C": 0, "D": 45}},
]

st.sidebar.title("🔄 Simulation Controls")
simulate = st.sidebar.button("Start Simulation")
delay = st.sidebar.slider("Delay between steps (seconds)", 1, 5, 2)

if simulate:
    st.sidebar.success("Simulation started...")

    for junc in junctions:
        st.subheader(junc["name"])

        # Create map centered at junction
        fmap = folium.Map(location=junc["location"], zoom_start=16)

        # Get vehicle data
        vehicles = junc["vehicles"]
        non_zero = {k: v for k, v in vehicles.items() if v > 0}

        if not non_zero:
            priority = None
        else:
            priority = min(non_zero, key=non_zero.get)  # Direction with least vehicles

        # Show color markers
        for dir, count in vehicles.items():
            color = "green" if dir == priority else "red" if count > 0 else "gray"
            folium.CircleMarker(
                location=junc["location"],
                radius=12,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.9,
                popup=f"Side {dir}: {count} vehicles",
            ).add_to(fmap)

        # Show map
        st_data = st_folium(fmap, width=700, height=500)
        time.sleep(delay)
else:
    st.info("Click 'Start Simulation' from the sidebar to begin.")
