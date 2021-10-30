# Este es el primer archivo de flask
# es lo mínimo que se necesita hacer pa que flask funcione
# además de lo siguiente se debe poner el siguiente comando en la terminal
# "export FLASK_APP=main.py" para linux
# "set FLASK_APP=main.py" para cmd
# "$env:FLASK_APP="main.py"" para powershell
# por lo anterior es recomendable crear un venv, lo cual hice para este caso
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def hola():
    miIP = request.remote_addr
    return f'hola mundo y Flask!, mi ip es {miIP}'
# CORRER CON "flask run" DENTRO DE LA TERMINAL

# Flask no tiene el debug prendido en un inicio, haciendo que tengamos que cerrar y abrir el servidor constantemente, pa arreglar eso se tiene que poner en la terminal
# "export FLASK_DEBUG=1"

# if __name__ == '__main__':
#     app.run(debug=True)