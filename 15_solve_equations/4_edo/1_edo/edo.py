from sympy import *

t = symbols('t', positive = True, real = True)
x = Function('x', real = True)
v = diff(x(t), t)
a = diff(v, t)
m = symbols('m', positive = True, real = True)
F = symbols('F', real = True)
w = symbols('w', positive = True, real = True)
b = symbols('w', positive = True, real = True)

posicion = dsolve(m*a - F*sin(w*t) - b*v, ics={x(0): 0, v.subs(t,0): 0})

print()
print("x =", posicion.args[1], "\n")
velocidad = posicion.args[1].diff(t)
print("v =", velocidad, "\n")
aceleracion = posicion.args[1].diff(t, 2)
print("a =", aceleracion, "\n")




#diffeq = Eq(y(x).diff(x,2)+2*y(x).diff(x)+2*y(x), exp(-x)+x**2+sin(x))
#ecuacion_fisica = Eq(m*a , F*sin(w*x))

#solucion = dsolve(ecuacion_fisica, x)

#ics={x(0): 0, v.subs(t,0): 0}

#solucion_v = dsolve(Derivative(m*a - F*sin(w*x), v))
#print(solucion_v)
