import sympy as sp

x, y = sp.symbols("x, y")
f = sp.Function("f")(x)

# podemos hacer una aproximación de Taylor (Serie)
serie = sp.series(f, x)
print(serie)