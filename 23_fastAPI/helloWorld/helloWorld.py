# para correr esto tienes que entrar obligatoriamente al entorno virtual
# se debe poner en la terminal "uvicorn helloWorld:app --reload"

# esto es pa definir que algun campo de mi clase es opcional
from typing import Optional
# esto viene con python, sirve pa enumerar supongo(?)
from enum import Enum  # esto es un tipo de dato exótico


# importo pydantic
from pydantic import BaseModel  # con esto puedo crear modelos
from pydantic import Field
# pydantic tiene muchos tipos de datos, por ejemplo uno que solo acepte emails, direccion de una página,número de tarjeta, etc...
# voy a poner 2 aqui
from pydantic import HttpUrl, EmailStr

# importo fastapi
from fastapi import FastAPI
from fastapi import Body, Query, Path

# la renombro pa que no sea molesto escribir todo el rato FastAPI()
app = FastAPI()


############ clase de tipos de cabello pa poder poner opciones pa la clase person #################

class HairColor(Enum):
    white = "white"
    brown = "brown"
    blonde = "blonde"
    black = "black"
    red = "red"

############ Modelos (son clases pa API's) ###############

# con Field() puedo validar los parametros directamente desde la clase Person o Location
# (validar = aplicar ciertas condiciones que si no cumple es rechazado)


class Person(BaseModel):
    firstName: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Tomilee"
    )
    lastName: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Blast"

    )
    age: int = Field(
        ...,
        gt=0,
        lt=115,
        example=21

    )
    # este valor es opcional, si se le pone algo debería ser un string, si no se pone na su valor es None (lo mismo que null)
    # Ahora hairColor solo puede ser un elemento de la clase HairColor
    hairColor: Optional[HairColor] = Field(
        default=None, example="black")  # este no lo carga bien por algun motivo
    # lo mismo pero debería tener como valor un boleano
    isMarried: Optional[bool] = Field(default=None, example=False)

    # me defino un ejemplo pa no tener que estar poniendolo todo el rato
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Tomas",
    #             "last_name": "Yanez",
    #             "age": 30,
    #             "hair_color": "black",
    #             "is_married": False
    #         }
    #     }


class Location(BaseModel):
    city: str
    state: str
    country: str


# esto es una path operation
# cuando estoy en la pestaña principal lo que hago es recibir hello: world


@app.get("/")
def home():
    return {"hello": "world"}
# (la path operation es el conjunto por si acaso)

# request and response body


@app.post("/person/new")  # post sirve para enviar datos al servidor
# ... indica que es obligatorio el parametro person
def create_person(person: Person = Body(...)):
    return person


# Validaciones -> voy a recibir parámetros pero tienen que cumplir requisitos
# Aqui aplico validaciones de query parameters (parametros opcionales (aunque aqui "edad" no es opcional, pero es una excepcion a la regla))

@app.get("/person/detail")
def showPerson(
    # Query significa que son opcionales, tienen el signo de interrogacion
    # None es el default
    name: Optional[str] = Query(
        None, min_length=1, max_length=50, example="tom"),
    # los 3 puntos significa que el parámetro es obligatorio
    edad: str = Query(..., example="2398")
    # return {name: edad}
):
    return {name: edad}

# Validaciones pero con path parameters


@app.get("/person/detail/{person_id}")
def showPerson(
    # gt significa greater than
    person_id: int = Path(..., gt=0, example="148234")
):
    return {person_id: "holanda :)"}


# Validaciones pero con Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        example="09832"
    ),
    # esto significa que tiene que enviar un json (de alguna forma)
    person: Person = Body(...),
    # esto significa que tiene que enviar otro json (de alguna forma)
    # esto es de desafio, normalmente es solo una clase
    location: Location = Body(...)
):
    # dado que quiero enviar información de 2 archivos debo mezclarlos y enviarlos como uno
    # pero hay un problema, originalmente fastApi trata a los archivos como json y despues los pasa a dict y despues en la pag los pasa a json, asi que hay que pasarlos a dict manualmente para mezclarlos
    combinado = person.dict()
    combinado.update(location.dict())
    return combinado


# probando los tipos de datos exóticos (importados de pydantic)
@app.get("/exoticos")
def datosExoticos(
    email: EmailStr = Query(...),
    sitioWeb: HttpUrl = Query(...)
):
    return {email: sitioWeb}
