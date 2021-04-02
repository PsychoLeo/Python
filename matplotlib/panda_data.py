import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url, header=None)

df.head(5)
df.tail(5)

df.dtypes
df.describe(include='all')
df.info()
 # command should be written in the interactive shell