# error de sintaxis, es decir, se cambiaron palabras, letras, etc...
# tambien son conocidos como typo (proviene de typographical error
# que se traduce como error tipográfico)
# Ej:
#for i on range(6):
#    print(i)
# output: SyntaxError: invalid syntax

# EXCEPCIONES: son otro tipo de error, a diferencia de lo anterior el 
# programa ya está corriendo y en algun punto falló algo que impide 
# su continuación
# hay más de 50 pero veamos las siguientes

# keyboardInterrupt: es cuando corre el programa pero lo detenemos desde
# el teclado con Ctrl+c
# Ej: hice un bucle infinito
#i=1
#while(i<2):
#    print("a") 
# output: KeyboardInterrupt 

# keyError: error al no encontrar un indice
# Ej:
#dict = {"nombre": "tomas",
#        "edad": 21}
#print(dict["cumpleaños"])   
# output: KeyError: 'cumpleaños'

# IndexError: error al no encontrar el indice de una lista
# Ej:
#lista = [28372, "hola", 3.14]
#print(lista[3])
# output: IndexError: list index out of range

#FileNotFoundError: el archivo que intentamos traer no lo encuentra
# Ej:
#with open("./notoy.txt", "r") as archivo:
#    print(archivo)
# output: FileNotFoundError: [Errno 2] No such file or directory: './notoy.txt'

# ZeroDivisionError: error al dividir por 0
# Ej
x = 1/0
# output: ZeroDivisionError: division by zero

# ModuleNotFoundError: intentamos importar un módulo y no lo encuentra
#import hola_no_soy_un_modulo as hnsum
# output: ModuleNotFoundError: No module named 'hola_no_soy_un_modulo'



# TRACEBACK: es lo que nos entrega python al tener un arror
# se traduce como "traza del error" que viene a significar
# "donde cree python que esta el error a partir de su busqueda"
# Ej:

# Traceback (most recent call last):
#  File "errores_que_avisan.py", line 43, in <module>
#    x = 1/0
#ZeroDivisionError: division by zero

# se debe leer de final a inicio