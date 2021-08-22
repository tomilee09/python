import pandas as pd

####importamos primero los datos que necesitamos####
df = pd.read_csv('poblacion.csv')
print(df)

#hacemos que los numeros se vean con un mejor formato
pd.options.display.float_format = '{:,.0f}'.format
print(df)

#tomamos una muestra de todos los paices
df_chile_argentina = df['Country'].isin(['Chile', 'Argentina'])
print(df[df_chile_argentina])