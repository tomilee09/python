import sympy as sp  

a, b, x, y = sp.symbols("a, b, x, y")
f = sp.Function("f")(x)

# podemos hacer una integral indefinida
integral_f = sp.integrate(f)
# ej:
print(sp.integrate(sp.sin(x)))


# podemos hacer una integral definida 
integral_def_f = sp.integrate(f, (x, a, b))
#ej: 
print(sp.integrate(sp.sin(x), (x, a, b)))

# podemos hacer integrales con limites en el infinito
print(sp.integrate(sp.exp(-x**2), (x, 0, sp.oo)))

# podemos integrar una expresion
expresion = x**2 + x + 1
print(sp.integrate(expresion))

# podemos hacer integrales con varias variables
expresion_x_y = x**2 + x + 1 + y + y**2
print(sp.integrate(expresion_x_y, x))
print(sp.integrate(expresion_x_y, y))
print(sp.integrate(expresion_x_y, x, y))

# podemos hacer integrales definidas
print(sp.integrate(expresion_x_y, (x, 0, 1), (y, 0, 1)))