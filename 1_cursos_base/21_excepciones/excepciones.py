# intenta mostrar 1/x en la terminal
x=0 # imagina eso lo pusiste tú
try:
    print(1/x)
# excepto si te sale el siguiente error, en ese caso imprime el siguiente
# texto en la pantalla
except ZeroDivisionError:
    print("dividiste por 0")

# imaginemos que queremos que algo sea considerado como un error
# ej: queremos obtener el doble de un numero
def doble(n):
    return 2*n
print(doble("hola")) # no queremos que esto corra, queremos solo numeros
# para que lo anterior sea un numero ponemos lo siguiente

def doble_solo_numeros(n):
    # intenta hacer lo siguiente
    try:
        # si n es string entonces fuerza a que haya una excepcion específica
        if type(n) == str:
            raise ValueError("ingresa solo numeros")
        # si lo anterior no ocurre regresa 2*n
        return 2*n
    # si ocurre una excepcion de tipo ValueError has lo siguiente
    except ValueError as mensaje_valueError:
        # imprimo lo que escribí anteriormente que tenia que decir
        return mensaje_valueError
print(doble_solo_numeros("texto"))

# finally: se usa para algo que siempre queramos que ocurra haya un error
# o no
try:
    print("este es el try")
except ValueError:
    print("este es el except")
finally:
    print("este es el finally")