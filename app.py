import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("🚦 Dynamic Traffic Light Simulation on Chandigarh Map")

# Dummy data: replace or expand as needed
junctions = [
    {"name": "Sector 42", "lat": 30.7133, "lon": 76.7366, "vehicles": {"A": 50, "B": 20, "C": 2, "D": 80}},
    {"name": "Sector 41", "lat": 30.7195, "lon": 76.7427, "vehicles": {"A": 10, "B": 0, "C": 30, "D": 25}},
    {"name": "Sector 40", "lat": 30.7260, "lon": 76.7471, "vehicles": {"A": 5, "B": 15, "C": 0, "D": 8}},
    {"name": "Sector 39", "lat": 30.7328, "lon": 76.7513, "vehicles": {"A": 12, "B": 30, "C": 9, "D": 0}},
    {"name": "Sector 21", "lat": 30.7355, "lon": 76.7766, "vehicles": {"A": 0, "B": 18, "C": 40, "D": 10}},
]

# Session state setup
if 'simulation_started' not in st.session_state:
    st.session_state.simulation_started = False
    st.session_state.current_junction = 0

# Show start or next button
if not st.session_state.simulation_started:
    if st.button("🚀 Start Simulation"):
        st.session_state.simulation_started = True
else:
    if st.session_state.current_junction < len(junctions):
        junction = junctions[st.session_state.current_junction]
        st.subheader(f"🧭 Junction {st.session_state.current_junction + 1} - {junction['name']}")

        # Determine direction to give green
        sorted_dirs = sorted(junction['vehicles'].items(), key=lambda x: -x[1])
        directions = [d for d, c in sorted_dirs if c > 0]
        green_order = directions if directions else ["None"]

        st.markdown(f"**Vehicle counts:** {junction['vehicles']}")
        st.markdown(f"✅ **Green light order**: {', '.join(green_order)}")

        # Show map
        m = folium.Map(location=[junction['lat'], junction['lon']], zoom_start=16)
        folium.Marker(
            [junction['lat'], junction['lon']],
            popup=f"{junction['name']} - Green: {green_order[0]}",
            icon=folium.Icon(color='red', icon='circle'),
        ).add_to(m)
        st_folium(m, width=700, height=500)

        if st.button("➡️ Next Junction"):
            st.session_state.current_junction += 1
    else:
        st.success("✅ Simulation complete! No more junctions.")
        if st.button("🔁 Restart"):
            st.session_state.simulation_started = False
            st.session_state.current_junction = 0
