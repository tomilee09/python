import nltk
import re
# previamente descargamos desde el ejecutable de python3 (abrir python en la terminal) unos archivos para probar nltk, que contienen enunciados de noticias llamado 'cess_esp'
# re es para las expresiones regulares

corpus = nltk.corpus.cess_esp.sents()

# obtenemos todas las palabras en vez de listas de palabras
flatten = [w for l in corpus for w in l] 

# con lo anterior hecho podemos ocupar la lista de palabras y buscar con re.search('filtro_con_regex', palabra_por_filtrar)
palabrasFiltradas = [w for w in flatten if re.search('^es', w)]
print(palabrasFiltradas[:10])

#texto tokenizado = texto ya separado en solo palabras
# vamos a tokenizar el siguiente texto
texto = """ Cuando sea el rey del mundo (imaginaba él en su cabeza) no tendré que  preocuparme por estas bobadas. 
           Era solo un niño de 7 años, pero pensaba que podría ser cualquier cosa que su imaginación le permitiera 
           visualizar en su cabeza ...""" 

# podemos separar por espacios vacios
print(re.split(r' ', texto)) # la r es para que interprete lo de dentro de las comillas como texto plano, porque dentro se pondran luego caracteres especiales
print()
# pero hay cosas que no son palabras como "\n" o "(imaginaba"

# la mejor forma de tokenizar es con el siguiente patron
pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][.,;"'?():-_`]    # Hace match con signos de puntuación
'''
# y con regexp_tokenize(texto, patron)
print(nltk.regexp_tokenize(texto, pattern))