import streamlit as st
import requests

st.set_page_config(page_title="Iris Species Classifier", layout="centered")

st.title("Iris Flower Classifier")
st.markdown("Enter the measurements to predict the species of the Iris flower.")

with st.form("iris_form"):
    sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, step=0.1, format="%.1f")
    sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, step=0.1, format="%.1f")
    petal_length = st.number_input("Petal length (cm)", min_value=0.0, step=0.1, format="%.1f")
    petal_width = st.number_input("Petal width (cm)", min_value=0.0, step=0.1, format="%.1f")

    submitted = st.form_submit_button("Predict Species")

    if submitted:
        api_url = "http://127.0.0.1:8000/predict"
        input_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        try:
            response = requests.post(api_url, json=input_data)
            if response.status_code == 200:
                json_response = response.json()
                if "predicted_class" in json_response:
                    prediction = json_response["predicted_class"]
                    st.success(f"Predicted Class: **{prediction}**")
                else:
                    st.error(f"Error in response: {json_response}")
        except Exception as e:
            st.error(f"Request Failed: {e}")
