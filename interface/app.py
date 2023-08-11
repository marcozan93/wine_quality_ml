import streamlit as st
import requests
import pandas as pd
from PIL import Image

kevin = Image.open("kevin.jpg")
michael = Image.open("michael.jpg")

def run():
    st.title("Predicting the quality of a wine :wine_glass:")
    st.markdown("This app uses a lasso regression model to predict the \
                quality of a wine based on the total sulfur dioxide value. \
                After fitting the model, this was the only variable maintained by \
                the model.")
    st.markdown("The quality of a wine is rated between 1 and 10, with higher values\
                suggesting a higher quality.")
    sulf_diox = st.slider("Select a value of total sulfur dioxide:", 1, 500, 
                          key="total_sulfur_dioxide")
    data = {"total_sulfur_dioxide": sulf_diox}
    if st.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        response.raise_for_status()
        prediction = response.json()

        st.success(f"The predicted quality of the wine is: **{round(prediction['prediction'],2)}**")
        if prediction['prediction'] >= 5:
            st.image(kevin)
        else:
            st.image(michael)

if __name__ == "__main__":
    run()