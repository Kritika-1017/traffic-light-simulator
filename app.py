
import streamlit as st
import pandas as pd
import time

st.title("🚦 Dynamic Traffic Light Simulation - Chandigarh")

st.markdown("""
This app simulates adaptive traffic light behavior at key junctions from Sector 42 to Sector 21 in Chandigarh.  
At each junction, vehicle counts from four directions are analyzed. The side with the fewest vehicles gets green first, and directions with zero vehicles are skipped.
""")

junctions_data = {
    "Junction 1 (Sector 42)": {"A": 50, "B": 20, "C": 2, "D": 80},
    "Junction 2": {"A": 0, "B": 30, "C": 10, "D": 15},
    "Junction 3": {"A": 25, "B": 0, "C": 5, "D": 40},
    "Junction 4": {"A": 10, "B": 5, "C": 0, "D": 60},
    "Junction 5 (Sector 21)": {"A": 15, "B": 45, "C": 20, "D": 0},
}

if st.button("Start Simulation"):
    for j_name, traffic_data in junctions_data.items():
        st.header(f"🚧 {j_name}")
        st.write("Initial vehicle counts:", traffic_data)

        non_empty_directions = {k: v for k, v in traffic_data.items() if v > 0}
        sorted_dirs = sorted(non_empty_directions.items(), key=lambda x: x[1])

        with st.container():
            for direction, count in sorted_dirs:
                st.success(f"🟢 GREEN light for direction {direction} — {count} vehicles")
                time.sleep(1.5)
                st.info(f"🔴 RED light for direction {direction}")
                time.sleep(0.8)
        
        st.markdown("---")

    st.balloons()
    st.success("Simulation completed! 🎉")
