# los generadores son suggar sintax de los iteradores
# los generadores son creados como funciones, a excepción de que se usa 
# la palabra clave "yield" en vez de "return". 
# yield en vez de terminar la función la pausa en esa posición
# podemos tener muchos yield en un generador
# Ej:
def generador():
    print("primer mensaje")
    n = 0 # valor de ejemplo pa que devuelva yield
    yield n
    print("segundo mensaje")
    n = 1
    yield n

# lo siguiente no va a funcionar porque debemos instanciar el generador
# (como si fuera una clase o como si estuvieramos aplicando el metodo iter)
# podemos verlo como que el generador "genera" objetos de la clase iterador
print(next(generador()))
print(next(generador()), "\n")

# instanciamos el iterador a partir del generador
miIterador = generador()
print(next(miIterador))
print(next(miIterador))



# Ejemplo fibonaci con generadores
def generador_fibonaci(n):
    """Esta función entrega todos los números de fibonaci hasta n"""
    n0, n1 = 0, 1
    contador = 0 
    while contador < n:
        yield n0
        n0, n1 = n1, n0+n1
        contador += 1

iterador_fibonaci_hasta_10 = generador_fibonaci(10)
for i in iterador_fibonaci_hasta_10:
    print(i)

