dictionary = {
    'yo': "soy yo po y que tanto",
    'lore': "la beibi ma hermosa",
    'canela_y_luly': "las mejores perritas",
}

print(dictionary['yo'])

print(dictionary['lore'])

print(dictionary['canela_y_luly'])

# tenemos diferentes palabras para imprimir las cosas dentro de los diccionarios
# llaves
for key in dictionary.keys():
    print(key)

# valores
for values in dictionary.values():
    print(values)

# los 2 anteriores, a lo cual llamamos items
for key, value in dictionary.items():
    print(f'mi llave es {key} y su valor es: {value}')