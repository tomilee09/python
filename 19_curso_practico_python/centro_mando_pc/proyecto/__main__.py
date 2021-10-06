### PARA CORRER EL PROYECTO SE DEBE ENTRAR EN EL AMBIENTE VIRTUAL Y PONER EN LA TERMINAL "PROYECTO" ###
# El siguiente programa esta creado mediante el paradigma de programacion orientada a procedimientos

import datetime
import time
# from PyDictionary import PyDictionary
# dictionary=PyDictionary()
import pandas as pd
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # esto es solo pa no mostrar el inicio de pygame
import pygame


def tocar_musica(nombre_cancion):
    """Mediante pygame.mixer reproduce musica, compatible con el wsl2"""
    pygame.init()
    pygame.mixer.music.load(nombre_cancion)
    pygame.mixer.music.play(1)



def poner_alarma(hora, minuto, motivo = "motivo no anotado"):  
    """permite guardar una alarma en el documento alarmas.csv, para que estas suenen se debe ejecutar la funcion 'activar alarmas'"""
    df = pd.read_csv("alarmas.csv", index_col=0)
    alarma = {'hora': hora, 'minuto': minuto, 'motivo': motivo}
    df = df.append(alarma, ignore_index=True)
    df.to_csv('alarmas.csv')


def activar_alarmas():    
    """si esta se mantiene activa irá tomando la hora cada 5 segundos, si esta coincide con alguna de las alarmas contenidas
    dentro del archivo 'alarmas.csv' se reproducirá un sonido y desplegará un mensaje en pantalla"""
    df = pd.read_csv("alarmas.csv")
    horas = df["hora"]
    minutos = df["minuto"]
    motivos = df["motivo"]
    while True:
        hora_actual = datetime.datetime.now()  
        for i in range(len(df)):
            if hora_actual.hour == horas[i] and hora_actual.minute == minutos[i]:
                print(f'Son las {int(horas[i])}:{int(minutos[i])}, {motivos[i]}')
                tocar_musica("./jagger.wav")
        time.sleep(5) # esto lo hago pa no usar tanto el procesador #tiempo se mide en segundos



# def palabra_ingles(palabra):
#     print (dictionary.translate(palabra,'es'))
#     print (dictionary.meaning(palabra))


def mostrar_alarmas():
    """muestra las alarmas contenidas en 'alarmas.csv'"""
    df = pd.read_csv("alarmas.csv")
    print(df)


def eliminar_alarma(indices):
    """elimina una o varias alarmas contenidas en 'alarmas.csv' según los índices ingresados"""
    df = pd.read_csv("alarmas.csv")
    df = df.drop(indices, axis=0)
    df.to_csv('alarmas.csv')


def bienvenida():
    """mensaje de bienvenida de la aplicación"""
    print("Bienvenido a el centro de acciones del PC, ¿Que deseas hacer?")
    print("presiona n para hacer [n]ada y que el programa corra en segundo plano")
    print("presiona a para [a]ñadir una alarma")
    print("presiona p para imprimir una [p]alabra")
    print("presiona r para mantener [r]unneando la app")
    print("presiona m para [m]ostrar las alarmas")
    print("presiona d para [d]eletear alarmas")
    print("presiona Ctrl + c para salir")


def posibles_acciones():
    """mensaje de posibles acciones dentro de la aplicación"""
    print("Las acciones que puedes realizar son las siguientes: ")
    print("presiona n para hacer [n]ada y que el programa corra en segundo plano")
    print("presiona a para [a]ñadir una alarma")
    print("presiona p para imprimir una [p]alabra")
    print("presiona r para mantener [r]unneando la app")
    print("presiona m para [m]ostrar las alarmas")
    print("presiona d para [d]eletear alarmas")
    print("presiona Ctrl + c para salir")


def main():
    """acciones que realiza la aplicación. La cree para que la abriera setup.py"""
    bienvenida()
    while True:
        comando = input(">>> ")
        if comando == "n":
            pass
        # if comando == "p":
        #     palabra = input("Ingrese la palabra: ")
        #     palabra_ingles(palabra)
            
        if comando == "m":
            mostrar_alarmas()

        if comando == "a":
            hora = int(input("Ingrese la hora: "))
            minuto = int(input("Ingrese el minuto: "))
            motivo = input("Ingrese el motivo: ")
            poner_alarma(hora, minuto, motivo)
        
        if comando == "d":
            indices = int(input("Ingrese el indice de la alarma que desea borrar: "))
            eliminar_alarma(indices)

        if comando == "r":
            print("esperando alarmas...")
            activar_alarmas()

        if comando == "?":
            posibles_acciones()


if __name__ == '__main__':
    main()