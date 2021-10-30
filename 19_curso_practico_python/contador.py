from time import sleep

def contador():
    """Es un contador simple, muestra los segundos y minutos"""
    segundos = 0
    minutos = 0
    while True: 
        # print(segundos, end = "\r") if minutos == 0 else print(f'{minutos}:0{segundos}', end = "\r") if segundos < 10 else print(f'{minutos}:{segundos}', end = "\r")
        # quedaría más entendible con un elif
        if minutos == 0:
            print(segundos, end = "\r")
        elif segundos < 10:
            print(f'{minutos}:0{segundos}', end = "\r")
        else:
            print(f'{minutos}:{segundos}', end = "\r")
        segundos+=1
        if segundos== 60:
            minutos+=1 
            segundos = 0
        sleep(1) # espero 1 segundo

contador()