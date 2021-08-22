#esto sirve pa hacer la aprox de una raiz que se le indique

epsilon = 0.01
inicio = 0.0
iteracion = 0.0
raiz = 0.0

numero = int(input('ingrese un numero que desee encontrar su raiz: '))

while numero - raiz**2 > epsilon:
    raiz = raiz + epsilon
else:
    print(f'la raiz es {raiz}')
