def factorial(numero):
    if numero < 2:
        factorial=1
    return numero * factorial (numero - 1)
numero = int(input("escribe un numero: "))
print(factorial(numero))

#def suma(a, b):
#    return a+b
#x=int(input("escribe un numero: "))
#y=int(input("escribe otro numero: "))
#print(suma(x,y))