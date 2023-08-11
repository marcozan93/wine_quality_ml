# wine_quality_ml
App to predict the quality of wines.

Technologies: python, sklearn, fastAPI, Streamlit, Docker (in progress).

The structure of the repo is as follows:
```
├───backend
│   └─── LassoModel.pkl
|   └─── main.py
├───data
|   └─── WineQT.csv
└───interface
    └─── app.py

```
- <code>app</code> folder includes the fastAPI code.
- <code>data</code> folder includes the data used for model training and testing.
- <code>interface</code> folder incldues the frontend of the streamlit app.
- <code>notebook_predictions.ipynb</code> was used to cerate the model.

## To run the app locally:
1. Go into the folder of the fastAPI app and run the following command:
    \wine_quality_ml\app>uvicorn main:app --host 127.0.0.1 --port 8000 --reload
This will run your API locally.

2. Go into the folder of the streamlit app and run the following command:
    \wine_quality_ml\interface>streamlit run app.py
This will run the streamlit app locally on http://192.168.1.210:8501

These two actions should be performed on two different terminals.
