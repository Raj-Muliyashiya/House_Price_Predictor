from fastapi import FastAPI
import joblib
import json
import numpy as np
import pandas as pd
from pydantic import BaseModel


model = joblib.load("model/house_price_pedictor.pkl")
columns = json.load(open("model/columns.json"))["data_columns"]

app = FastAPI()

class houseinput(BaseModel):
    location : str
    bhk : int
    total_sqft : float
    bath : int
    

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

        x_df = pd.DataFrame([x],columns=columns)

        prediction = model.predict(x_df)[0]

        return {"the prediction is ":prediction}

    except Exception as e:
        return {'Error': str(e)}



