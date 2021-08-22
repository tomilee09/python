import random
from bokeh.plotting import figure, output_file, show

def roll_dice(number_roll=1):
    i=0
    global list_rolls
    list_rolls = list([])
    while i<number_roll:
        valor_dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        list_rolls.append(valor_dado_1)
        i+=1
    return list_rolls

def average(list_rolls=[1]):
    return sum(list_rolls)/number_roll


def plot(x=[1], y=[1]):
    output_file("line.html")
    p = figure(plot_width=400, plot_height=400)
    p.line(x, y, color="navy")
    show(p)

if __name__ == '__main__':
    number_roll = int(input('cuantas veces quieres que el dado se tire?: '))
    roll_dice(number_roll)
    eje_x = list(range(number_roll))
    plot(eje_x, list_rolls)
    print(average(list_rolls))