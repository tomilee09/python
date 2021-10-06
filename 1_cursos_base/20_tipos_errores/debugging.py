# Errores de Lógica

# se debugea cuando tenemos un error que no es intrinseco de python, sino
# que el programa corre pero no hace lo que deseamos
# Ej: queremos crear una funcion que imprima numeros impares y multiplos
# de 5
def numeritos(n):
    for i in range(n+1):
        if i%2==0 and i%5==0:
            print(i)
numeritos(10)

# y esto se debugea con el debugeador de vscode