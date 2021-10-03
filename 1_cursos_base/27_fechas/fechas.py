import datetime as dt

hora_actual = dt.datetime.now() # la hora de mi pc
print(hora_actual) 
print(hora_actual.hour) # puedo seleccionar la hora
print(hora_actual.minute) # puedo seleccionar los minutos

# para pedir diferentes zonas horarias (horas diferentes a las de mi pc) podemos usar la libreria pytz
import pytz
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones para ver los timezones de cada pais
zona_horaria_argentina = pytz.timezone("Europe/London") # la parte de "Europe/London" es lo que hay que ver en la pagina y cambiar
hora_argentina = dt.datetime.now(zona_horaria_argentina)
print(hora_argentina)