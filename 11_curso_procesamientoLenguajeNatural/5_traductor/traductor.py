from nltk.corpus import swadesh

# esta es la cantidad de idiomas
print(swadesh.fileids())

# estas son algunas palabras en ingles que conoce swadesh
print(swadesh.words('en'))

# ahora vamos a crear un traductor ingles-español
en2es = swadesh.entries(['en', 'es'])
translate = dict(en2es)
print(translate['dog'])