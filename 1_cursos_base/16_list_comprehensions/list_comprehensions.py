# forma anticuada, mala, del diaulo, con virus, uso 4 lineas
cuadrados_diabolicos = []
for x in range(4, 11):
    if x%3==0:
        cuadrados_diabolicos.append(x**2)
print(cuadrados_diabolicos)

# forma pro de crear listas, uso una linea
miLista = [x**2 for x in range(4, 11) if x%3==0] # if es opcional
print(miLista)

miLista = [x for x in range(0, 9999) if x%36==0] # if es opcional
print(miLista)

# pa que aprenderlo?
# porque ahorras espacio, mucho más entendible, además de poder entender
# código de terceros que te puedes encontrar en internet