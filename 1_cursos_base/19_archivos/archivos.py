# open es para abrir el archivo, le pongo el nombre del archivo, que solo
# tiene permisos pa leerlo ("r") y que lo llame miTxt
# El "with" es una palabra reservada de python que -en resumen- sirve pa
# que el archivo no se corrompa al cerrarse repentinamente, o que algo
# falle en mi código, tiene que ver con los "try" y "except" pero no 
# cacho muy bien como, de todas formas es obligatorio poner el with 
# al leer un archivo
# encoding utf-8 es pa que reciba tildes
with open("./holi.txt", "r", encoding= "utf-8") as miTxt:
    lineas = [linea for linea in miTxt]
    print(lineas)

# podemos crear otro archivo y ponerle texto
with open("./otroTxt.txt", "w", encoding= "utf-8") as otroTxt:
    otroTxt.write("hola\n")

with open("./otroTxt.txt", "a", encoding= "utf-8") as otroTxt_alFinal:
    otroTxt_alFinal.write("esto se escribe al final de mi archivo original\n")
