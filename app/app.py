import streamlit as st
import joblib
import os

model_folder = "models"


heating_model_path = os.path.join(model_folder, "heating_model.pkl")
cooling_model_path = os.path.join(model_folder, "cooling_model.pkl")

heating_model = joblib.load(heating_model_path)
cooling_model = joblib.load(cooling_model_path)

st.title("Building Energy Load Predictor")
st.markdown("""
This tool predicts the **Heating Load** and **Cooling Load** of a building 
based on geometry and material choices.

It also estimates total annual energy use (kWh) and cost (€) based on your building size
and local energy price.
""")

st.header("Geometry Parameters")
relative_compactness = st.slider("Relative Compactness", 0.5, 1.0, 0.8, step=0.01)
surface_area = st.number_input("Surface Area (m²)", value=700.0, step=10.0)
wall_area = st.number_input("Wall Area (m²)", value=300.0, step=10.0)
roof_area = st.number_input("Roof Area (m²)", value=150.0, step=5.0)
overall_height = st.number_input("Overall Height (m)", value=7.0, step=0.1)

orientation_dict = {"North": 2, "East": 3, "South": 4, "West": 5}
orientation_name = st.selectbox("Building Orientation", list(orientation_dict.keys()))
orientation = orientation_dict[orientation_name]

st.header("Window Parameters")
glazing_area = st.slider("Glazing Area Ratio", 0.0, 0.4, 0.2, step=0.01)
glazing_dist_dict = {
    "No glazing": 0,
    "North wall only": 1,
    "East wall only": 2,
    "South wall only": 3,
    "West wall only": 4,
    "Uniform on all walls": 5
}
glazing_dist_name = st.selectbox("Glazing Area Distribution", list(glazing_dist_dict.keys()))
glazing_area_dist = glazing_dist_dict[glazing_dist_name]

st.header("Material Choices")
wall_type_dict = {
    "Brick, no insulation": 0,
    "Brick, insulated": 1,
    "High-performance wall": 2
}
roof_type_dict = {
    "Concrete slab, no insulation": 0,
    "Concrete slab, insulated": 1,
    "Green roof": 2
}
window_type_dict = {
    "Single glazing": 0,
    "Double glazing": 1,
    "Triple glazing": 2
}

wall_type_name = st.selectbox("Wall Type", list(wall_type_dict.keys()))
roof_type_name = st.selectbox("Roof Type", list(roof_type_dict.keys()))
window_type_name = st.selectbox("Window Type", list(window_type_dict.keys()))

wall_type = wall_type_dict[wall_type_name]
roof_type = roof_type_dict[roof_type_name]
window_type = window_type_dict[window_type_name]

st.header("Energy Price")
energy_price = st.number_input("Energy Price (€/kWh)", value=0.20, step=0.01)

if st.button("Predict Energy Loads & Costs"):
    
    input_data = [[relative_compactness, surface_area, wall_area,
                   roof_area, overall_height, orientation,
                   glazing_area, glazing_area_dist,
                   wall_type, roof_type, window_type]]

    
    heating_load_per_m2 = heating_model.predict(input_data)[0]
    cooling_load_per_m2 = cooling_model.predict(input_data)[0]

   
    floor_area = surface_area  
    total_heating_energy = heating_load_per_m2 * floor_area
    total_cooling_energy = cooling_load_per_m2 * floor_area

    
    heating_cost = total_heating_energy * energy_price
    cooling_cost = total_cooling_energy * energy_price

    
    st.subheader("Predicted Energy Loads")
    st.write(f"**Heating Load (per m²):** {heating_load_per_m2:.2f} kWh/m²")
    st.write(f"**Cooling Load (per m²):** {cooling_load_per_m2:.2f} kWh/m²")

    st.subheader("Total Annual Energy Use")
    st.write(f"**Total Heating Energy:** {total_heating_energy:,.0f} kWh/year")
    st.write(f"**Total Cooling Energy:** {total_cooling_energy:,.0f} kWh/year")

    st.subheader("Estimated Annual Energy Costs")
    st.write(f"**Heating Cost:** €{heating_cost:,.2f}/year")
    st.write(f"**Cooling Cost:** €{cooling_cost:,.2f}/year")
    st.write(f"**Total Energy Cost:** €{(heating_cost + cooling_cost):,.2f}/year")
