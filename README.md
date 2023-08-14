# wine_quality_ml
App to predict the quality of wines.

Technologies: python, sklearn, fastAPI, Streamlit, Docker.

The structure of the repo is as follows:
```
├───docker-compose.yml
├───backend
│   └─── RFModel.pkl
|   └─── main.py
|   └─── Dockerfile
├───data
|   └─── WineQT.csv
└───interface
    └─── app.py
    └─── Dockerfile
```
- <code>app</code> folder includes the fastAPI code and its associated Dockerfile.
- <code>data</code> folder includes the data used for model training and testing.
- <code>interface</code> folder incldues the frontend of the streamlit app including its associated Dockerfile.
- <code>notebook_predictions.ipynb</code> was used to cerate the model.

## To run the app locally using docker compose:
Open a terminal (cmd), make sure that docker daemon is running, then run:<br>
<code>docker compose build</code><br>
and successively<br>
<code>docker compose up</code>
