import sympy as sp 

# podemos derivar con .diff()
x = sp.Symbol('x')
f = sp.Function('f')(x)
derivada = sp.diff(f, x) # equivalente a f.diff(x)

# podemos hacer dobles, triples o en general n derivadas agregando indices
doble = sp.diff(f, x, x)

y = sp.Symbol('y')
derivada_x_y = sp.diff(f, x, y)
derivada_y_x = sp.diff(f, y, x)
muchas_derivadas = sp.diff(f, x, y, x, x, x, y)

# para no escribir tantos indices podemos usar numeros
muchas_derivadas = f.diff(x, 4, y, 2) # si la funcion es continua

# podemos derivar una  expresion 
expresion = x**2 + 3*x + 1
derivada_expresion = expresion.diff(x)
print(derivada_expresion)

# podemos tener una expresion que aun no ha sido derivada y despues derivarla con .doit()
derivada2 = sp.Derivative(sp.exp(sp.cos(x)), x)
print(derivada2.doit())