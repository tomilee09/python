### PARA CORRER EL PROYECTO SE DEBE ENTRAR EN EL AMBIENTE VIRTUAL Y PONER EN LA TERMINAL "PROYECTO" ###
# este archivo sirve para instalar un proyecto dentro de pip con el comando "pip3 install -e ." o "pip3 install --editable ."
# que mas o menos significa "pip instala los archivos editables en este directorio"
# este archivo indica que es un editable y que archivos usa (en este caso los de la carpeta "proyecto")
from setuptools import setup

setup(
    name="proyecto",
    version="0.1.0",
    packages=["proyecto"],
    entry_points={
        "console_scripts": [
            "proyecto = proyecto.__main__:main"
        ]
    },
)
# console_scripts debe contener la funcion base que vamos a llamar, que en este caso es la funcion main que está dentro del archivo
# __main__ que a su vez está dentro del directorio proyecto, esto es lo que abriremos cada vez que pongamos "proyecto" en la terminal