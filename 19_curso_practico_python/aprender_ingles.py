import pygame
from traductor import *
import pandas as pd
import pickle
import io
import os

def word_by_number(number):
    df = pd.read_csv("word-meaning-examples.csv")
    return df["Word"][number]

def meaning_by_number(number):
    df = pd.read_csv("word-meaning-examples.csv")
    return df["Meaning"][number]

def example_by_number(number, number_example):
    df = pd.read_csv("word-meaning-examples.csv")
    if type(df[f'Examples/{number_example}'][number]) == type("texto"):
        return df[f'Examples/{number_example}'][number] 
    else:
        return ""


pygame.init()

#DEFINO COSAS
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
green = [0, 255, 0]
blue = [0, 0, 255]
RED = [255, 100, 100]
reloj = pygame.time.Clock()
SIZE = [600, 400]
screen = pygame.display.set_mode(SIZE)

# creo esta variable para guardar el número en el cual quedé
global numero_palabra
with open('mypickle.pk', 'rb') as archive:
    if os.stat("mypickle.pk").st_size != 0:
        numero_palabra = pickle.load(archive)  
    else:
        numero_palabra = 0

# Lo siguiente será la configuración del texto
# indico la tipografía y tamaño del texto
font = pygame.font.Font('freesansbold.ttf', 32)
espaciado = 50

palabra_ingles = font.render('texto_inicio', True, green, blue)
traduccion = font.render('texto_inicio', True, green, blue)
significado = font.render('texto_inicio', True, green, blue)
ejemplo1 = font.render('texto_inicio', True, green, blue)
ejemplo2 = font.render('texto_inicio', True, green, blue)
ejemplo3 = font.render('texto_inicio', True, green, blue)
ejemplo4 = font.render('texto_inicio', True, green, blue)
ejemplo5 = font.render('texto_inicio', True, green, blue)

palabra_inglesRect = palabra_ingles.get_rect()
palabra_inglesRect.center = (SIZE[0]/2, SIZE[1]/2)

traduccionRect = traduccion.get_rect()
traduccionRect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + espaciado)

significadoRect = significado.get_rect()
significadoRect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 2*espaciado)

ejemplo1Rect = ejemplo1.get_rect()
ejemplo1Rect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 3*espaciado)

ejemplo2Rect = ejemplo2.get_rect()
ejemplo2Rect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 4*espaciado)

ejemplo3Rect = ejemplo3.get_rect()
ejemplo3Rect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 5*espaciado)

ejemplo4Rect = ejemplo4.get_rect()
ejemplo4Rect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 6*espaciado)

ejemplo5Rect = ejemplo5.get_rect()
ejemplo5Rect.center = (SIZE[0]/5 + espaciado, SIZE[1]/2 + 7*espaciado)


def run():
    # Core del programa
    # tomo la palabra y la traduzco
    palabra = word_by_number(numero_palabra)
    palabra_traducida = traducir(palabra, "en", "es")
    textoSignificado = meaning_by_number(numero_palabra)
    textoEjemplo1 = example_by_number(numero_palabra, 1)
    textoEjemplo2 = example_by_number(numero_palabra, 2)
    textoEjemplo3 = example_by_number(numero_palabra, 3)
    textoEjemplo4 = example_by_number(numero_palabra, 4)
    textoEjemplo5 = example_by_number(numero_palabra, 5)

    # cambio los textos que muestro en pantalla
    palabra_ingles = font.render(f'{palabra}', True, blue, green)
    traduccion = font.render(f'translate: {palabra_traducida}', True, blue, green)
    significado = font.render(f'meaning: {textoSignificado}', True, blue, green)
    ejemplo1 = font.render(textoEjemplo1, True, blue, green)
    ejemplo2 = font.render(textoEjemplo2, True, blue, green)
    ejemplo3 = font.render(textoEjemplo3, True, blue, green)
    ejemplo4 = font.render(textoEjemplo4, True, blue, green)
    ejemplo5 = font.render(textoEjemplo5, True, blue, green)
    
    # seleccionar la imagen de fondo
    pagina = f'https://www.google.com/search?q={palabra}&tbm=isch'
    imagen_palabra = obtener_imagen(pagina)
    img = io.BytesIO(imagen_palabra)
    imagen_fondo = pygame.image.load(img)


    #actualizar pantalla
    screen.fill(RED) # color de fondo
    screen.blit(imagen_fondo, [SIZE[0], SIZE[1]/2-2*espaciado])
    screen.blit(palabra_ingles, palabra_inglesRect)
    screen.blit(traduccion, traduccionRect)
    screen.blit(significado, significadoRect)
    screen.blit(ejemplo1, ejemplo1Rect)
    screen.blit(ejemplo2, ejemplo2Rect)
    screen.blit(ejemplo3, ejemplo3Rect)
    screen.blit(ejemplo4, ejemplo4Rect)
    screen.blit(ejemplo5, ejemplo5Rect)

try:
    corriendo = True
    run() # para que cuando abra el programa muestre la palabra en que quedé
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
            # lo siguiente es lo que pasa cuando se mantiene pulsada una tecla
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    numero_palabra += 1
                    run()
                if evento.key == pygame.K_DOWN:
                    numero_palabra -= 1
                    run()
        pygame.display.flip() # muestro todo lo anterior en pantalla
        reloj.tick(30) #le digo que haga todo lo anterior cada 1/60 [s], es decir, que vaya a 60FPS
# lo último que hace el archivo es guardar el dato "numero_palabra"
# lo hará si termina de forma normal o si hay un error, es decir, siempre
finally:
    with open('mypickle.pk', 'wb') as archive:
        pickle.dump(numero_palabra, archive)
