import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20201219', periods=6, freq='W')

# dataframe from numpy array
df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list("ABCDE"))

print(df)

