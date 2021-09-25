# este código sirve para correr un fibonaci de forma recursiva, lo que hará será que a partir de un número x entregue su correspondiente valor de fibonaci
def fibonaci(x):
    # defino dos casos base (tal como se hace matemáticamente en la sucesión)
    # esto lo hago para que al momento de ir retrocediendo la función tenga una base (no se vaya a los números negativos), lo usaré más adelante
    if x == 1:
        return 1 # si no sabes python, estas dos lineas de código se pueden traducir como "si x es igual a 1, entonces el resultado de la funcion es 1"
    if x == 2:
        return 1 # lo mismo que antes pero con x igual a 2
    # aqui está la magia, digo que mi resultado es igual a fibonaci de x-1 sumado con fibonaci de x-2, lo cual sabemos que es cierto por la matemática,
    # pero 
    # ¿como el programa sabe cuanto valen esos 2 valores?, pues, al comenzar la recursión, la función fibonaci(x-1) llamará a fibonaci(x-2) y fibonaci(x-3)
    # que a su vez para obtener su valor llamarán a fibonaci(x-4) fibonaci(x-5), y así ..., hasta llegar a fibonaci(3), que es igual a 
    # fibonaci(1) + fibonaci(2), de los cuales ya sabemos sus valores (1 y 1), con lo cual sabemos que fibonaci(3) = fibonaci(1) + fibonaci(2) = 2, pero 
    # ya que sabemos fibonaci(3)
    # podemos saber fibonaci(4), pues es igual a fibonaci(2) + fibonaci(3), y de esa forma sucesivamente podemos encontrar todos los valores de la sucesion
    # de fibonaci hasta conocer fibonaci(x)
    resultado = fibonaci(x-1) + fibonaci(x-2)
    # aqui simplemtente digo que el valor que entrega mi funcion es la variable resultado
    return resultado

# muestro el valor de fibonaci de 10 en pantalla
print(fibonaci(10))