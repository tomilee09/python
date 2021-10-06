# python desde la version 3.9 viene con la opcion de tipado estático
# es decir, puedo decirle que una variable es int
entero: int = 5 # equivalente a "entero = 5"
print(entero)

decimal: float = 3.14 # equivalente a "decimal = 3.14"
print(decimal)

texto: str = "hola" # equivalente a "texto = "hola""
print(texto)

# podemos hacer esto con listas, tuplas y diccionarios importandolas desde
# el modulo typing (viene preinstalado en python)
from typing import List, Dict, Tuple
numeros: List[int] = [1, 2, 3, 4, 5]
print(numeros)

tupla: Tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
tupla2: Tuple[int, str, float] = (1, "miTexto", 2.71) # como las tuplas son inmutables puedo ponerle el tipo a cada uno de los elementos
print(tupla)
print(tupla2)

diccionario: Dict[int, int] = {i:i**2 for i in range(1, 6)}
print(diccionario)

# puedo hacer esto dentro de una función
def suma(a: int, b: int) -> int:
    return a+b
print(suma(10, 20))
# pero como esto es nuevo, no está 100% asentado en python, asi que si
# pongo un string como entrada igual va a funcionar
print(suma("10", "20"))

# si corro esto con python3 me va a decir que esta de pana
# pero si corro esto con mypy (sudo apt install mypy) me tira error
# por cierto mypy fue creado por el creador de python (al menos vi
# el proyecto en su github)
# poner "mypy tipado_estatico.py" y va a decir los problemas