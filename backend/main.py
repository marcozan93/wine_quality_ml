from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
import uvicorn


app = FastAPI(title="Wine quality prediction",
              version = "0.1",
              description="Lasso model that predicts the quality of the wine.")

class WineData(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

model = pickle.load(open("RFModel.pkl", "rb"))

@app.get("/")
@app.get("/home")
def read_home():
    """
        Home endpoint which can be used to test the availability of the applciation.
    """
    return {"message": "System is healthy."}

@app.post("/predict")
async def predict(data: WineData):
    new_input = pd.DataFrame(np.array([[data.fixed_acidity,
                           data.volatile_acidity,
                           data.citric_acid,
                           data.residual_sugar,
                           data.chlorides,
                           data.free_sulfur_dioxide,
                           data.total_sulfur_dioxide,
                           data.density,
                           data.pH,
                           data.sulphates,
                           data.alcohol]]),
                columns=["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
                        "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density",
                        "pH", "sulphates", "alcohol"])
    pred = model.predict(new_input)[0]
    
    return {"prediction": pred}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)