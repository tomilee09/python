import sympy as sp  

# podemos calcular el limite de sin(x)/x -> 0
x = sp.Symbol('x')
print(sp.limit(sp.sin(x)/x, x, 0)) # =1

# con esto podemos trabajar con la definición de derivada
h = sp.Symbol('h')
f = sp.Function('f') # con f una funcion cualquiera 
definicion_derivada = (f(x+h)-f(x))/h

# ahora calculamos algunos limites tendiendo h a 0. usamos subs() para sustituir a f por otra funcion
print(sp.limit(definicion_derivada.subs(f, sp.cos), h, 0))
print(sp.limit(definicion_derivada.subs(f, sp.sin), h, 0))