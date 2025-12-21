import numpy as np
import pandas as pd
import json

columns = json.load(open("model/columns.json"))["data_columns"]


x = np.zeros(len(columns))
print(x)