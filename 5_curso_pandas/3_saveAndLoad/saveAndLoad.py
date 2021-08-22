import pandas as pd

######creamos un dataframe para guardar#######

diccionario = {'tomas':[1, 2, 3], 'lore':[4, 5, 6], 'papa':[7, 8, 9]}
dataFrame = pd.DataFrame(diccionario)
print(dataFrame, "\n")

######ahora si a guardar######

dataFrame.to_csv('/mnt/c/Users/tomilee/Desktop/python/5_curso_pandas/3_saveAndLoad/test.csv')
dataFrame.to_csv('test2.csv')

#guardar sin el indice
dataFrame.to_csv('test3.csv', index = False)

#para leer estos archivos
datos = pd.read_csv('test3.csv')
print(datos, '\n')

#en csv el separador es ',', este separador podemos cambiarlo
dataFrame.to_csv('test4.csv', sep ='|', index = False)

#para leerlo tengo que indicar de nuevo el separador
datos_barrita = pd.read_csv('test4.csv', sep = '|')
print(datos_barrita, '\n')

#######guardar en diferentes formatos########
#guardar en excel
dataFrame.to_excel('test5.xlsx', index = False)

#leer un excel
datos_excel = pd.read_excel('test5.xlsx')
print(datos_excel, '\n')

#guardar en json
dataFrame.to_json('test6.json')

#leer un json
datos_json = pd.read_json('test6.json')
print(datos_json, '\n')

#guardar en pickle
dataFrame.to_pickle('test7.pkl')

#leer un pickle
datos_pkl = pd.read_pickle('test7.pkl')
print(datos_pkl, '\n')

#guardar en parquet
dataFrame.to_parquet('test8.parquet')

#leer un parquet
datos_parquet = pd.read_parquet('test8.parquet')
print(datos_parquet, '\n')

#guardar en hdf
dataFrame.to_hdf('test9.hdf', key = 'data', format ='table')

#leer un hdf
datos_hdf = pd.read_hdf('test9.hdf')
print(datos_hdf, '\n')