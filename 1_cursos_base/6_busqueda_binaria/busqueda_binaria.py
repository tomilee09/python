# este codigo sirve pa encontrar raices y está mucho más optimizado que "aprox_raiz.py"

numero = int(input('ingrese un numero que desee encontrar su raiz: '))
epsilon = 0.01
inicio = 0.0
final = max(1.0,numero)
raiz = (inicio + final) / 2

while abs(numero - raiz**2) >= epsilon:
    if raiz**2 < numero:
        inicio = raiz
    else:
        final = raiz
    raiz = (inicio + final) / 2
print(f'la raiz es {raiz}')