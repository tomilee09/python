ll = ['hola', 'hola', 'mundo', 'tengo' , 'frio', 'si', 'si']
print(set(sorted(ll)))
print(sorted(set(ll)))

import pandas as pd
df = pd.DataFrame()
df["col1"] = [1, 2, 3]
df["col2"] = [1, 2, 3]
df["col3"] = [1, 2, 3]
df["col4"] = df["col1"]/(df["col2"]*df["col3"])
print(df)