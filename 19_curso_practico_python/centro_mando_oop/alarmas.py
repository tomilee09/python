# voy a crear las alarmas las cuales van a tener las caracteristicas de hora, minuto, motivo, cancion, prendida
# tendrán los métodos de activarse, sonar, quedarse en espera

import threading # NOTA: este threading corre todo en un solo nucleo, asi que puedo crear tantos como yo quiera. Para correr cosas en paralelo usar multiprocessing
from datetime import datetime # para fijar las horas de la alarma
from time import sleep # para que no se ejecute todo el rato el programa ocupando mucho procesador
# lo siguiente es para importar pygame sin que salga el texto de inicio
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # esto es solo pa no mostrar el inicio de pygame
import pygame # importo pygame para usar mixer, que es pa tocar musica


def tocar_musica(nombre_cancion):
    pygame.init()
    pygame.mixer.music.load(nombre_cancion)
    pygame.mixer.music.play(1)


class Alarma:
    """Su intención es crear alarmas que se ejecuten al mismo tiempo"""
    def __init__(self, hora, minuto, motivo = "motivo no indicado", cancion = "jagger.wav", prendida = 1):
        # los atributos que se le debe ingresar a una alarma al momento de crearse son:
        self.hora = hora
        self.minuto = minuto
        self.motivo = motivo
        self.cancion = cancion
        self.prendida = prendida # voy a usar esto pa no tener que estar borrando las alarmas


    def mecanismo_alarmas(self):
        while self.prendida == 1:
            # print(threading.current_thread()) descomentar para comprobar que los threads funcionan
            hora_actual = datetime.now()  
            if hora_actual.hour == self.hora and hora_actual.minute == self.minuto:
                print(f'Son las {self.hora}:{self.minuto}, pusiste esta alarma por: {self.motivo}')
                tocar_musica(self.cancion)
            sleep(5) # esto lo hago pa no usar tanto el procesador #tiempo se mide en segundos
    

    def run(self):
        threading.Thread(target=self.mecanismo_alarmas).start()


    def on(self):
        self.prendida = 1


    def off(self):
        self.prendida = 0
        
# NOTA: esto es claramente menos engorroso que el anterior, sin tener en cuenta que ambos tienen objetivos distintos (uno da opciones en tiempo real y este está
# hecho para usarse en otro archivo de python (main.py)), este tiene mayor claridad, se nota más la intencionalidad, para que sirve cada variable, donde se definen,
# además de tener el plus de no tener que usar un archivo .csv, así que podemos ver directamente las alarmas que tenemos en el archivo de python en el que 
# se ejecuta la clase