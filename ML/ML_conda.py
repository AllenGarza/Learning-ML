import numpy as np
import pandas as pd
import sys
import os

url =  'https://data.cdc.gov/resource/vbim-akqf.json'
data = pd.read_json(url)

race = data.iloc[:, 5]
infected = data.iloc[3]
print(list(data.columns.values))


