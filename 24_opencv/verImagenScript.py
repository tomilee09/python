# ADVERTENCIA: ESTO NO FUNCIONA CON WSL, HAY QUE CORRERLO DESDE EL PYTHON DE WINDOWS, CREE UN ALIAS PA ESO
# EN VEZ DE PONER "python3" PONER "pywin"

# esto sirve para mostrar la imagen en pantalla y cerrarlo simplemente apretando "q" en el teclado


import cv2
img = cv2.imread("rgb.jpeg")

# muestro la imagen
cv2.imshow("perro", img)
# while True:
#     # si pasa al menos 1 milisegundo (pa que no se cierre altiro) y presionamos "q" se cierra el ciclo
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
cv2.waitKey(0)
cv2.destroyAllWindows()
