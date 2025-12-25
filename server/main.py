from fastapi import FastAPI, HTTPException
import joblib
import json
import numpy as np
import pandas as pd
from pydantic import BaseModel, Field


model = joblib.load("model/house_price_pedictor.pkl")

with open("model/columns.json", "r") as f:
    columns = json.load(f)["data_columns"]

app = FastAPI()

class houseinput(BaseModel):
    location : str = Field(..., description="Location of the house in Bangalore")
    bhk : int = Field( ..., gt=0,lt=10)
    total_sqft : float = Field(..., gt=0)
    bath : int = Field(..., gt=0,lt=10)
    

datas = []

@app.get('/')
def home():
    return "This is the home"

@app.post('/predict_home_price')
def predict(houseinput :houseinput):
    try: 
        x = np.zeros(len(columns))
        
        x[columns.index('bhk')] = houseinput.bhk
        x[columns.index('total_sqft')] = houseinput.total_sqft
        x[columns.index('bath')] = houseinput.bath

        loc = houseinput.location.lower()

        if loc in columns:
            loc_index = columns.index(loc)
            x[loc_index] = 1
        else:
            raise HTTPException(status_code=400, detail="Location not recognized")

        x_df = pd.DataFrame([x],columns=columns)

        prediction = model.predict(x_df)[0]

        return {"the prediction is ":prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/get_locations')
def get_locations():
    try:
        location_list = columns[3:]
        if  not location_list:
            raise HTTPException(status_code=404, detail="No Location Found")
        
        return { "location" : location_list }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   