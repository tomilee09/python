DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# AQUI COMIENZA LOS EJERCICIOS
trabajadores = [x["name"] for x in DATA]
trabajadores_hof = list(map(lambda x:x["name"] , DATA)) # lo mismo pero con hof
print(trabajadores)
print(trabajadores_hof)

pythoners = [x["name"] for x in DATA if x["language"]=="python"]
pythoners_hof = list(filter(lambda x: x["language"]=="python", DATA)) # lo mismo pero con hof
pythoners_hof = list(map(lambda x:x["name"] , pythoners_hof)) 
# tuve que usar 2 porque con la primera seleccioné los que tenian python y con la segunda me quedé solo con los nombres
print(pythoners)
print(pythoners_hof)

adultos_mayores = [x["name"] for x in DATA if x["age"]>=60]
adultos_mayores_hof = list(filter(lambda x: x["age"]>=60, DATA))
adultos_mayores_hof = list(map(lambda x: x["name"], adultos_mayores_hof))
print(adultos_mayores)
print(adultos_mayores_hof)