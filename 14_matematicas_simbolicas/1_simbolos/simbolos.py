import sympy as sp

# esto hace que los outputs sean mas bonitos aparentemente
sp.init_printing()

# creamos el símbolo x, es decir, la variable x ahora representa un simbolo abstracto matemático
x = sp.Symbol("x")

# si queremos que sea menos abstracto podemos indicarselo, ej: decir que es positivo
y = sp.Symbol("y", positive = True)

# podemos decirle: real, imaginary, positive, negative, integer, odd, even, prime, finite, infinite
# además podemos preguntarle y nos entregará true o false: .is_real, .is_imaginary, .is_...

# lo anterior nos sirve para que sympy no haga cosas inecesarias, ej:
print(sp.sqrt(x**2)) # sqrt(x**2), pues no sabe si es negativo
print(sp.sqrt(y**2)) # y

# otros ejemplos de la utilidad de ser específicos
n1 = sp.Symbol("n")
n2 = sp.Symbol("n", integer = 1)
n3 = sp.Symbol("n", odd = 1)

print(sp.cos(n1 * sp.pi)) # cos(pi*n)
print(sp.cos(n2 * sp.pi)) # (-1)**n
print(sp.cos(n3 * sp.pi)) # -1

# podemos crear varios simbolos de una (notese que ahora dice Symbols en vez de Symbol)
a, b, c = sp.symbols('a,b,c')

# podemos crear numeros específicos en simpy (si operamos numeros normales con simbolos se transforman automagicamente en numeros de sympy)
i = sp.Integer(2309)
print(i.is_Integer, i.is_real, i.is_odd)

# para pasarlo a numeros de python normales solo hay que usar int()
print(type(int(i)), int(i))

# hay que diferenciar entre mayusculas y minusculas, integer representa un numero entero cualquiera y Integer representa un número entero en específico
i = sp.Symbol("i", integer = 1)
print(i.is_integer, i.is_Integer)

# podemos crear un float y decirle exactamente la presición que queremos darle
float1 = sp.Float(0.3, 25)
float2 = sp.Float('0.3', 25)
print(float1, float2) # notemos que si se lo damos con comillas no hay impresición, esto es porque aqui le damos directamente los numeros 0.3 como un string, en cambio sin las comillas le damos un float de python que trae una incerteza propia

# podemos crear números racionales
racional1 = sp.Rational(2, 3)
racional2 = sp.Rational(4, 5)
print(racional1, racional2)

# hay distintos otros simbolos matemáticos como sp.pi = pi, sp.E = e, sp.I = i, sp.oo = infinito

# podemos crear una función
funcion = sp.Function("f") # esta no está definida, pero podría servir para cuando conocemos la ecuación de la función pero no la función en si (o sea, para EDO's)

# podemos crear una función definida
seno = sp.sin(4 * sp.pi)
print(seno)

# podemos crear funciones de forma paramétrica con lambda
h = sp.Lambda(x, x**2)
print(h(5))

# podemos crear expresiones con sympy
expresion = 2* (x**2 - x) - x*(x+1)
print(expresion) 


# con sympy podemos simplificar una expresión facilmente (no solo polinomios, tambien trigonometricas y exponenciales)
print(sp.simplify(expresion))

# si queremos hacer lo inverso podemos expandir 
expresion2 = (x+1)**4
print(expresion2.expand())

# expand tiene muchos argumentos, ej: trig
expresion_trig = sp.sin(x+y).expand()
print(expresion_trig)
expresion_trig = sp.sin(x+y).expand(trig = True)
print(expresion_trig)

# podemos expandir los logaritmos
k,l = sp.symbols("k, l", positive = 1)
exp_log = sp.log(k*l).expand(log = True)
print(exp_log)

# expandir complejos
exp_complex = sp.exp(sp.I*k + l).expand()
print(exp_complex)
exp_complex = sp.exp(sp.I*k + l).expand(complex = True)
print(exp_complex)

# expandir con mul=True significa hacer todas las multiplicaciones, su inverso es sp.factor()
exp = x**4 + 4*x**3 + 6*x**2 + 4*x + 1
exp_factor = exp.factor()
print(exp_factor)

# al igual que en la seccion anterior podemos ser específicos con lo que queremos factorizar, aunque ahora hay que usar nuevas funciones
print(sp.logcombine(exp_log))

# en caso de no poder factorizar podemos agrupar los terminos de un elemento con .collect(termino)
exp_nocolectada = x + y + x*y
print(exp_nocolectada.collect(x))
print(exp_nocolectada.collect(y))

# por otro lado podemos trabajar con fracciones parciales, con sp.apart() podemos separar en fracciones parciales, y con sp.together() podemos unirlas en una sola
fraccion = 1/(x**2 + 3*x + 2)
print(sp.apart(fraccion, x))

# con sp.cancel() podemos cancelar terminos de una expresión
print(sp.cancel(y/(y*x+y)))

# podemos reemplazar un simbolo por otro con .subs(simbolo1, simbolo2)
exp_sub = x+y
print(exp_sub)
exp_sub = (x+y).subs(x, y)
print(exp_sub) # 2*y

# por último en la parte de los números, podemos evaluar números simplemente con un parentesis
print(h(3.4))
# o tambien con sp.N
print(h(sp.pi)) # no se da un resultado numérico
print(h(sp.N(sp.pi))) # si da un resultado numérico

# de hecho podemos usar numpy y evaluar muchos resultados, pero previamente hay que poner que es de numpy con la función sp.lambdify()
import numpy as np 
h = sp.lambdify(x, x**2, 'numpy')
valores = np.arange(0, 10)
print(h(valores))