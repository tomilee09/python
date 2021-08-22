import sympy as sp   
x = sp.Symbol('x')

# podemos resolver una expresion cualquiera
print(sp.solve(x**2 + 2*x -3)) # asumimos x**2 + 2*x -3 == 0

# podemos resolver una eq de segundo grado cualquiera
a, b, c = sp.symbols("a, b, c")
print(sp.solve(a*x**2 + b*x + c, x))

# podemos resolver una ecuacion con trigonométricas
print(sp.solve(sp.sin(x) - sp.cos(x), x))

# pero hay ecuaciones que simplemente no puede resolver
print(sp.solve(x**5 - x**2 + 1))

# podemos resolver un sistema de ecuaciones
y = sp.Symbol('y')
eq1 = x + 2*y -1
eq2 = x - y + 1
print(sp.solve([eq1, eq2], [x, y]))