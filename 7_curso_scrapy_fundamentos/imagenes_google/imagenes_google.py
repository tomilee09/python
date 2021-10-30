# web scrappins is useful to excract things from internet
# I need this course to extract images from internet to create a interactive dictionary
# requests library is useful to use http
# beautifulSoup use HTML
# Selenium make phantom site webs and create bots
# scrapy is useful for... something

# la siguiente es la ruta de html para llegar hasta las imágenes, la busqué a mano
RUTA = '//a/div/img/'
# con @alt se obtiene el texto de las imágenes
# poner @src para obtener las imagenes
# pd: para encontrarlo tuve que poner lo siguiente en la terminal de chrome
# $x('//a/div/img/@src').map(x => x.value)

# la pagina que usé es google imagenes y busqué "gato"
PAGINA = "https://www.google.com/search?q=gato&hl=en&tbm=isch&sxsrf=AOaemvKFgy3V20LMivVphCfaq6ehsQr9FA%3A1633830270196&source=hp&biw=767&bih=704&ei=fkViYaP1CZSz5OUPz5SeuAU&ved=0ahUKEwijrIGH3L7zAhWUGbkGHU-KB1cQ4dUDCAc&uact=5&oq=gato&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCCMQ7wMQ6gIQJ1C8EVizEmCmGGgBcAB4AIABKYgBjgGSAQE0mAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img"
WIKIPEDIA = "https://es.wikipedia.org/wiki/F%C3%ADsica"
# de aqui en adelante hago el scraping
import requests
import lxml.html as html

XPATH_IMAGES = '//a/div/img/@src'
XPATH_WIKITEXT = "//p/text()"

def obtener_datos(pagina, xpath):
    # lo que almacenará respuesta_peticion es todo el documento html de la página
    respuesta_peticion = requests.get(pagina)
    # lo siguiente almacena el texto html de forma correcta (puede procesar la ñ por ejemplo)
    textoHtmlPagina = respuesta_peticion.content.decode('latin-1')
    # transformo el texto plano anterior en un texto en el que pueda usar xpath
    htmleado = html.fromstring(textoHtmlPagina)
    datos_finales = htmleado.xpath(xpath)
    print(datos_finales)


def obtener_datos_utf8(pagina, xpath):
    # lo que almacenará respuesta_peticion es todo el documento html de la página
    respuesta_peticion = requests.get(pagina)
    # lo siguiente almacena el texto html de forma correcta (puede procesar la ñ por ejemplo)
    textoHtmlPagina = respuesta_peticion.content.decode('UTF-8')
    # transformo el texto plano anterior en un texto en el que pueda usar xpath
    htmleado = html.fromstring(textoHtmlPagina)
    datos_finales = htmleado.xpath(xpath)
    print(datos_finales)


# el del video puso más cosas pero prefiero ponerlo despues pa no emborronar la simpleza de obtener las imagenes
def obtener_datos_mejorado():
    # pongo el try y except porque podría fallar la carga de la pagina (fallar el método http)
    try:
        response = requests.get(PAGINA)
        # si http entrega el código 200 significa que todo salió bien, si es cualquier otro código pasó algo
        if response.status_code == 200:
            home = response.content.decode('utf-8')
        else:
            raise ValueError(f'Error: {response.status}')
    # mostramos el error que dió http en la terminal
    except ValueError as ve:
        print(ve)



if __name__ == '__main__':
    obtener_datos(PAGINA, XPATH_IMAGES)
    # obtener_datos_utf8(WIKIPEDIA, XPATH_WIKITEXT) obtiene el texto de la página de wikipedia, es mucho texto