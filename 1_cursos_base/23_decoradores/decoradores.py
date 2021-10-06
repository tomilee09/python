# un decorador es un closure
# que es un closure?
# es una funcion con otra funcion anidada (nested en ingles)
# además la funcion nested debe referenciar a una variable del scope superior
# la función que envuelve a la nested function debe retornar a la nested function
# un ejemplo de closure es el siguiente
def repetir_palabra(x):
    def veces_repetir(y): 
        return x*y
    return veces_repetir

repetir_Tomas = repetir_palabra("Tomas")
print(repetir_Tomas(5))

# nota: la regresion lineal en scikitlearn es un closure :O

# Ahora sí, los decoradores son closures, pero que reciben como parametro
# una función. Ej:
def decorador(funcion):
    def envoltura(): # tambien conocida como wrapper
        funcion() 
        print("Soy un decorador, tus deseos son mis ordenes")       
        print("🥳😎 ¡Decoracion! 😎🥳 \n")
    return envoltura

def mifuncionPorDecorar():
    print("Holi, ojalá me decoraran")

miFuncionDecorada = decorador(mifuncionPorDecorar)
miFuncionDecorada()

# podemos añadirle azucar sintactica al código (hacerlo más "leíble")
# en vez de poner
def holi():
    print("holi")
holi = decorador(holi)
holi()

# podemos poner lo siguiente
@decorador
def holanda():
    print("holanda")
holanda()

# Ejemplo practico decoradores:
def nombre_mayusculas(funcion):
    def wrapper(nombre):
        return funcion(nombre.upper())
    return wrapper

@nombre_mayusculas
def Saludo(nombre):
    return f'Hola {nombre}, espero tengas un buen dia \n'

print(Saludo("tomas"))


# Por último, podriamos tener un decorador que queramos aplicar a una gran
# variedad de funciones (ej: medir tiempo de ejecucion de la funcion),
# para ello haremos lo siguiente
def autoria(funcion):
    def wrapper(*args, **kwargs): # le ponemos args y kwargs
        print("Esta funcion fue hecha por Tomás")
        funcion(*args, **kwargs) # le ponemos args y kwargs
    return wrapper

@autoria
def suma(a, b):
    print(f'La suma es: {a+b}')
suma(3, 5)

# *args dice que no importa el numero de argumentos que tenga la funcion 
# original, simplemente tomalas y usalas
# **kwargs dice que no importa el numero de keyWordsArguments que tenga 
# la funcion original, simplemente tomalas y usalas 
# los keyword arguments son argumentos con nombre, por ejemplo 
# ej: def miFuncion(a = 2): ...

# un decorador útil: medir el tiempo de ejecución de cualquier función
from datetime import datetime
def execution_time(function):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        function(*args, **kwargs)
        final_time = datetime.now()
        dt = final_time-initial_time
        seconds = dt.total_seconds()
        print(f'El tiempo de ejecución fue de {seconds} segundos.')
    return wrapper

@execution_time
def ciclo_for(n):
    for _ in range(n):
        pass

ciclo_for(10000000) # esto muestra cuanto se demora el ciclo for en correr