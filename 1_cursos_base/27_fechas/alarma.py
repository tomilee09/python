##### CORRER DESDE TERMINAL DE WINDOWS #####
# ejemplo practico, crear una alarma a las 13:00
import datetime as dt
from playsound import playsound # paquete pa emitir sonido mp3
sonido = "C:\\Users\\tomilee\\Desktop\\programacion\\python\\1_cursos_base\\27_fechas\\jagger.mp3"
while True:
    fecha = dt.datetime.now()
    if fecha.hour == 13 and fecha.minute >= 0:
        print("es la horaaa")
        playsound(sonido)
# para pararlo poner en el teclado: Ctrl + c