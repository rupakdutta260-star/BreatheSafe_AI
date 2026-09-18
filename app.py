import streamlit as st
import pandas as pd
import joblib


model, encoder = joblib.load("model.pkl")


st.set_page_config(

    page_title="BreatheSafe AI",
    page_icon="🌍",
    layout="wide"
)
st.title(" BreatheSafe AI")
st.write("Enter air quality values and predict the health risk.")
st.sidebar.header(" Enter Air Quality Values")
pm25 = st.sidebar.number_input(
    "PM2.5",
    min_value=0.0,
    value=30.0
)

pm10 = st.sidebar.number_input(
    "PM10",
    min_value=0.0,
    value=50.0
)
no2 = st.sidebar.number_input(
    "NO2",
    min_value=0.0,
    value=25.0
)
so2 = st.sidebar.number_input(
    "SO2",
    min_value=0.0,
    value=10.0
)
co = st.sidebar.number_input(
    "CO",
    min_value=0.0,
    value=0.5
)
o3 = st.sidebar.number_input(
    "O3",
    min_value=0.0,
    value=30.0
)
aqi = st.sidebar.number_input(
    "AQI",
    min_value=0,
    value=70
)
st.subheader("Air Quality Dashboard")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("PM2.5", pm25)

with col2:
    st.metric("PM10", pm10)

with col3:
    st.metric("NO2", no2)

with col4:
    st.metric("AQI", aqi)


col5, col6, col7 = st.columns(3)

with col5:
    st.metric("SO2", so2)

with col6:
    st.metric("CO", co)

with col7:
    st.metric("O3", o3)

st.subheader("Pollution Levels")
chart_data = pd.DataFrame({
    "Pollutant": ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"],
    "Value": [pm25, pm10, no2, so2, co, o3]
})
chart_data = chart_data.set_index("Pollutant")

st.bar_chart(chart_data)

st.subheader("Health Risk Prediction")
if st.button("Predict Health Risk"):
    input_data = pd.DataFrame({
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO2": [no2],
        "SO2": [so2],
        "CO": [co],
        "O3": [o3],
        "AQI": [aqi]
    })

    prediction = model.predict(input_data)


    result = encoder.inverse_transform(prediction)[0]

    # Show result
    if result == "Low":

        st.success("Health Risk: LOW")
    elif result == "Medium":
        st.warning("Health Risk: MEDIUM")
    else:
        st.error("Health Risk: HIGH")


    st.subheader("Input Data")
    st.dataframe(
        input_data,
        use_container_width=True
    )


st.write("---")
st.caption(
    "Air Quality Health Risk Prediction | "
)