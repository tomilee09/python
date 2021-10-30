# importo la libreria de google translator, es una api, es decir, es la misma app que esta en la web (o al menos eso entendí)
from googletrans import Translator

def traducir(texto = "nada", idioma_entrada = "es", idioma_salida = "en"):
    translator = Translator()
    texto_traducido = translator.translate(texto, src=idioma_entrada, dest = idioma_salida)
    return texto_traducido.text


# lo siguiente es para descargar y mostrar la imágen
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


def obtener_imagen(pagina):
    # lo que almacenará respuesta_peticion es todo el documento html de la página
    respuesta_peticion = requests.get(pagina)
    # transformo el texto plano anterior en un texto en el que pueda usar xpath
    sopa = BeautifulSoup(respuesta_peticion.text, "lxml") # le decimos que pasee usando lxml como referencia
    cuerpo_imagen = sopa.find_all("img", attrs = {"class":"yWs4tf"})[1]
    link_imagen = cuerpo_imagen.get("src")
    imagen_pedida = requests.get(link_imagen)
    return imagen_pedida.content


def mostrar_imagen(imagen):
    im = Image.open(BytesIO(imagen))
    plt.imshow(im)
    plt.show()


def imgGoogle(texto):
    pagina = f'https://www.google.com/search?q={texto}&tbm=isch'
    imagen = obtener_imagen(pagina)
    mostrar_imagen(imagen)


if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    
    idioma_entrada = input("Ingresa el idioma del texto (en: english, es: español, fr:french, it:italian, de (german), cn:chinese, gr:greek, jp:japanese, ru:russian): ")
    idioma_salida = input("Ingresa el idioma de salida (en: english, es: español, fr:french, it:italian, de (german), cn:chinese, gr:greek, jp:japanese, ru:russian): ")
    traduccion = traducir(texto, idioma_entrada, idioma_salida)
    print(traduccion)
    imgGoogle(texto)