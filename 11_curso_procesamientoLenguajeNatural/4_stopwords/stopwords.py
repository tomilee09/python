# una stopword es una palabra sin un significado por si misma
import nltk
nltk.download('book')
from nltk.book import *
from nltk.corpus import stopwords

# mostramos en pantalla las stopwords en español
stopwords_espanol = stopwords.words('spanish')
print(stopwords_espanol)

# por curiosidad, veamos le porcentaje de stopwords en un libro
stopwords_ingles = stopwords.words('english')
texto_sin_stopwords = [words for words in text1 if words.lower() not in stopwords_ingles]
total_palabras = text1
print(len(texto_sin_stopwords)/len(total_palabras))