import nltk
nltk.download('wordnet')
nltk.download('omw')
from nltk.corpus import wordnet

# synset: grupo de sinónimos
synset = wordnet.synsets('carro', lang = 'spa')
print(synset)

# a cada elemento del synset podemos verle su definición
for i in synset:
    print(i.name(), ": ", i.definition())

# podemos imprimir las distintas palabras que representan cada synset
print()
for i in synset:
    print(i.name(), ": ", i.definition())
    for j in i.lemma_names():
        print("  -  ", j)

# podemos pedir los hiponimos de la palabra (sinonimos pero que significan algo específico)
print(synset[0].hyponyms()) # con el [0] estamos tomando a "car"

# podemos analogamente pedir los hiperonimos(sinonimos con un significado más amplio)
print(synset[0].hypernyms())

# podemos calcular una "distancia" entre 2 sinsets, llamada similitud
animal = wordnet.synsets("animal", lang = 'spa') #esto entrega 3 definiciones, solo queremos la primera que significa "ser vivo"
animal = animal[0]

perro = wordnet.synsets("perro", lang = 'spa')
perro = perro[0]

gato = wordnet.synsets("gato", lang = 'spa')
gato = gato[0]

similaridad_perro_animal = perro.path_similarity(animal)
print(similaridad_perro_animal) # 0.3333...

similaridad_perro_gato = perro.path_similarity(gato)
print(similaridad_perro_gato) # 0.2

similaridad_perro_perro = perro.path_similarity(perro)
print(similaridad_perro_perro) # 1.0

# podemos concluir que lo más cercano que puede estar una palabra de otra es 1, y que mientras más se alejan menor es su similaridad