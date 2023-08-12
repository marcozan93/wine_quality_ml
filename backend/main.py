from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import uvicorn


app = FastAPI(title="Wine quality prediction",
              version = "0.1",
              description="Lasso model that predicts the quality of the wine.")

class WineData(BaseModel):
    total_sulfur_dioxide: float

model = pickle.load(open('LassoModel.pkl', 'rb'))

@app.get("/")
@app.get("/home")
def read_home():
    """
        Home endpoint which can be used to test the availability of the applciation.
    """
    return {"message": "System is healthy."}

@app.post("/predict")
async def predict(data: WineData):
    new_input = np.array([[0, 0, 0, 0, 0, 0, data.total_sulfur_dioxide, 0, 0, 0, 0]])
    pred = model.predict(new_input)[0]
    return {'prediction': pred}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)