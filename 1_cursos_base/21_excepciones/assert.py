# imagina quieres crear una funcion que solo sume numeros positivos,
# podemos poner un  try ... if a<0 or b<0: 
#                               raise ValueError("solo numeros positivos")
#                   ... except ...
# como vemos son muchas lineas, incluso si no usamos try-except
# con un if serian unas 3 lineas teniendo en cuenta el exit()
# assert soluciona eso, se escribe de la siguiente forma}
# assert condicion, mensaje_error
# se lee de la siguiente forma
# afirmo lo siguiente, si no se cumple envia este mensaje de error
def suma_numeros_positivos(a, b):
    assert a>0 and b > 0, "debes ingresar solo numeros positivos"
    return a+b
print(suma_numeros_positivos(-1, 2)) # eso dará un error