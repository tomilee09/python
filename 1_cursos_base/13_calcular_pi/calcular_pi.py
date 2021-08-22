import random

def put_needles(number_needles):
    number_needles_inside_circle = 0
    for _ in range(number_needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distance = (x**2 + y**2)**(0.5)
        if distance <= 1:
            number_needles_inside_circle += 1
    return 4*number_needles_inside_circle/number_needles

if __name__ == "__main__":
    number_needles = int(input("cuantas agujas?: "))
    print(put_needles(number_needles))