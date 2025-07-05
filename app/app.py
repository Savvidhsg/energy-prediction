import streamlit as st
import joblib

model_folder = os.path.join(os.path.dirname(__file__), "models")
heating_model_path = os.path.join(model_folder, "heating_model.pkl")
cooling_model_path = os.path.join(model_folder, "cooling_model.pkl")

heating_model = joblib.load(heating_model_path)
cooling_model = joblib.load(cooling_model_path)


st.title(" Building Energy Load Predictor")
st.markdown("""
This app predicts the **Heating Load (HL)** and **Cooling Load (CL)** of a building
based on geometry and material choices.

You can also estimate total annual energy use (kWh) and cost (€) based on your building size
and local energy price.
""")

st.header("📐 Geometry Parameters")
relative_compactness = st.slider("Relative Compactness", 0.5, 1.0, 0.75)
surface_area = st.slider("Surface Area (m²)", 400, 1000, 600)
wall_area = st.slider("Wall Area (m²)", 200, 400, 300)
roof_area = st.slider("Roof Area (m²)", 100, 300, 200)
overall_height = st.slider("Overall Height (m)", 3.0, 10.0, 5.0)
orientation = st.selectbox("Orientation", [2, 3, 4, 5])
glazing_area = st.slider("Glazing Area (%)", 0.0, 0.4, 0.1)
glazing_area_distribution = st.selectbox("Glazing Area Distribution", [0, 1, 2, 3, 4])

st.header("🏗 Material Parameters")
wall_type = st.selectbox("Wall Type", ["Standard Wall", "High Performance Wall"])
roof_type = st.selectbox("Roof Type", ["Standard Roof", "Green Roof"])
window_type = st.selectbox("Window Type", ["Single Glazing", "Double Glazing", "Triple Glazing"])

st.header("💵 Energy Price")
energy_price = st.number_input("Enter your local energy price (€/kWh)", min_value=0.05, max_value=1.00, value=0.20)

if st.button("Predict Energy Loads"):
    wall_type_encoded = 1 if wall_type == "High Performance Wall" else 0
    roof_type_encoded = 1 if roof_type == "Green Roof" else 0
    window_type_encoded = 1 if window_type == "Double Glazing" else 0

    input_features = [[
        relative_compactness, surface_area, wall_area, roof_area,
        overall_height, orientation, glazing_area, glazing_area_distribution,
        wall_type_encoded, roof_type_encoded, window_type_encoded
    ]]

    predicted_heating_load = heating_model.predict(input_features)[0]
    predicted_cooling_load = cooling_model.predict(input_features)[0]
    total_energy_kwh = predicted_heating_load + predicted_cooling_load
    total_cost = total_energy_kwh * energy_price
    
    st.success(f"🔥 **Predicted Heating Load:** {predicted_heating_load:.2f} kWh")
    st.success(f"❄️ **Predicted Cooling Load:** {predicted_cooling_load:.2f} kWh")
    st.info(f"💡 **Total Energy Consumption:** {total_energy_kwh:.2f} kWh")
    st.info(f"💸 **Estimated Annual Cost:** €{total_cost:.2f}")
