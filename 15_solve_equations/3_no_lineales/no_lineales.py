import sympy as sp    

# podemos resolver ecuaciones no lineales con sympy
x, a, b, c = sp.symbols("x, a, b, c")
solucion_baskara = sp.solve(a*x**2 + b*x + c, x)
print(solucion_baskara)

# no solo puede expresiones algebraicas
solucion_expresion_no_algebraica = sp.solve(a*sp.cos(x) - b*sp.sin(x), x)
print(solucion_expresion_no_algebraica)

# para otros casos debemos realizar métodos numéricos, usemos sympy
# método Newton-Raphson, x_i+1 = x_i - f(x_i)/f'(x_i)
funcion = x**2 - 1
derivada = sp.diff(funcion, x)

raiz = 3
i = 0
while i<5:
    raiz = raiz - funcion.subs(x, raiz)/derivada.subs(x, raiz)
    i = i + 1
    print(raiz)
# notamos que raiz tiende a 1, es decir llegamos a que la raiz está en 0

# esto mismo lo podemos realizar scipy
import scipy.optimize as op  
funcion_python = lambda x: x**2 -1
raiz_newton = op.newton(funcion_python, 3)
print(raiz_newton)

# scipy tiene muchos otros métodos numéricos, los 3 siguientes deben pasarseles 2 numeros a, b tal que el signo de f(a) sea distinto de f(b)
raiz_bisect = op.bisect(funcion_python, 0, 10) # le tenemos que pasar el intervalo donde busca
print(raiz_bisect)

raiz_brentq = op.brentq(funcion_python, 0, 10) # le tenemos que pasar el intervalo donde busca
print(raiz_brentq)

raiz_brenth = op.brenth(funcion_python, 0, 10) # le tenemos que pasar el intervalo donde busca
print(raiz_brenth)

# para resolver un sistema de ecuaciones no lineales hay que usar el jacobiano y de momento me da flojera