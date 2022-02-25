import turtle
import math
from os import name, system


COLOR = turtle.pencolor()
SPEED = turtle.speed()
WIDTH = turtle.width()


def set_values():
    turtle.pencolor(COLOR)
    turtle.speed(SPEED)
    turtle.width(WIDTH)


def square(a):
    turtle.penup()
    turtle.goto(- a / 2, a / 2)
    turtle.pendown()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)


def circle(r):
    set_values()
    turtle_step = 2 * math.pi * r / 360
    turtle.penup()
    turtle.goto(r / 2, 0)
    turtle.pendown()
    turtle.right(90)
    for i in range(180):
        turtle.forward(turtle_step)
        turtle.right(2)


def triangle(a):
    turtle.penup()
    turtle.goto(-a / 2, -(a / 2 * math.sqrt(3) / 3))
    turtle.pendown()
    for i in range(3):
        turtle.forward(a)
        turtle.left(120)


def hexagon(a):
    turtle.penup()
    turtle.goto(-a / 2, -a * math.sqrt(3) / 2)
    turtle.pendown()
    for i in range(6):
        turtle.forward(a)
        turtle.left(60)


def square_spiral(a):
    step = a / 10
    for i in range(1, 11):
        for j in range(2):
            turtle.forward(step * i)
            turtle.left(90)


def spiral(step):
    for i in range(36):
        for j in range(20):
            turtle.forward(step)
            turtle.left(6)
        step += 0.5


def cursor(a):
    turtle.penup()
    turtle.left(90)
    turtle.forward(a / 2)
    turtle.left(90)
    turtle.forward(a / 2)
    turtle.left(180)
    turtle.pendown()

    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a / 2 * math.sqrt(2))
    turtle.right(90)
    turtle.forward(a / 2 * math.sqrt(2))
    turtle.right(75)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)

    turtle.penup()
    turtle.forward(a / 2)
    turtle.right(90)
    turtle.forward(math.sqrt(3) / 2 * a)

    turtle.pendown()
    turtle.right(180)
    turtle.forward(math.sqrt(3) / 2 * a + a / 2)


def star(a):
    for i in range(8):
        cursor(a)
        turtle.right(360 / 8)


def duck():
    a = 100

    # голова
    for i in range(8):
        turtle.left(45)
        turtle.forward(a)

    # клюв
    turtle.pu()
    turtle.goto(-(a + a * math.sqrt(2) / 2), a / 2 + a * math.sqrt(2) / 2)
    turtle.pd()
    turtle.left(180)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(a / 2 * math.sqrt(2))
    turtle.left(135)
    turtle.forward(a / 2)
    turtle.pu()
    turtle.left(180)
    turtle.forward(a / 2)
    turtle.pd()
    turtle.left(135)
    turtle.forward(a / 2 * math.sqrt(2))
    turtle.left(45)
    turtle.forward(a / 2 + a)

    # тело
    turtle.pu()
    turtle.goto(a * math.sqrt(2) / 4, a * math.sqrt(2) / 4)
    turtle.pd()

    turtle.right(45)
    turtle.forward(a / 2)
    turtle.left(45)
    turtle.forward(3.5 * a)

    # Оперение
    turtle.right(135)
    for i in range(2):
        turtle.forward(a)
        turtle.right(45)
        turtle.forward(a)
        turtle.pu()
        turtle.left(180)
        turtle.forward(a)
        turtle.pd()
        turtle.right(135)

    turtle.forward(a)
    turtle.right(45)
    turtle.forward(3.5 * a - 3 * a * math.sqrt(2) / 2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a * math.sqrt(2) / 2)
    turtle.right(45)
    turtle.forward(a)

    # Тело
    turtle.pu()
    turtle.right(45)
    turtle.goto(a * math.sqrt(2) / 4, a * math.sqrt(2) / 4)
    turtle.right(45)
    turtle.forward(a / 2)
    turtle.left(45)
    turtle.forward(3.5 * a)
    turtle.right(135)
    turtle.forward(3 * a)
    turtle.pd()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a + a * math.sqrt(2) / 2 + (3.5 * a - 4 * a * math.sqrt(2) / 2))
    turtle.right(45)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a * math.sqrt(2))
    turtle.right(45)
    turtle.forward(a)

    # Глаз
    turtle.pu()
    turtle.left(45)
    turtle.forward(a * math.sqrt(2) / 2 + a)
    turtle.pd()
    turtle.right(90)
    for i in range(180):
        turtle.forward(2 * math.pi * (a / 2) / 360)
        turtle.right(2)


def menu():
    global COLOR, SPEED, WIDTH
    colors = ['black', 'red', 'blue', 'green', 'yellow', 'violet', 'cyan']
    shapes = ['square', 'circle', 'triangle', 'hexagon', 'archimedean spiral', 'square spiral',
              'cursor', 'star', 'duck']
    choose = ''
    while choose.lower() != 'exit' or choose != '0':
        system("cls" if name == 'nt' else 'clear')
        if choose.lower() in shapes:
            print(f'{choose.title()} was successfully drawn!\nTry something else!')
        choose = input('+----------------------------+\n'
                       '|         Turtle Menu        |\n'
                       '| Choose executable function |\n'
                       '| 1. Square                  |\n'
                       '| 2. Circle                  |\n'
                       '| 3. Triangle                |\n'
                       '| 4. Hexagon                 |\n'
                       '| 5. Archimedean spiral      |\n'
                       '| 6. Square spiral           |\n'
                       '| 7. Cursor                  |\n'
                       '| 8. Star                    |\n'
                       '| 9. Duck                    |\n'
                       '| S. Settings                |\n'
                       '| 0. Exit                    |\n'
                       '+----------------------------+\n'
                       'Answer: ')
        if choose.lower() == 'square' or choose == '1':
            choose = 'square'
            size = int(input('Input side size: '))
            while not size:
                size = int(input('Incorrect input!\n'
                                 'Input side size: '))
            turtle.reset()
            square(size)
        elif choose.lower() == 'circle' or choose == '2':
            choose = 'circle'
            size = int(input('Input radius size: '))
            while not size:
                size = int(input('Incorrect input!\n'
                                 'Input radius size: '))
            turtle.reset()
            circle(size)
        elif choose.lower() == 'triangle' or choose == '3':
            choose = 'triangle'
            size = int(input('Input side size: '))
            while not size:
                size = int(input('Incorrect input!\n'
                                 'Input side size: '))
            turtle.reset()
            triangle(size)
        elif choose.lower() == 'hexagon' or choose == '4':
            choose = 'hexagon'
            size = int(input('Input side size: '))
            while not size:
                size = int(input('Incorrect input!\n'
                                 'Input side size: '))
            turtle.reset()
            hexagon(size)
        elif choose.lower() == 'archimedean spiral' or choose == '5':
            choose = 'archimedean spiral'
            turtle.reset()
            spiral(1)
        elif choose.lower() == 'square spiral' or choose == '6':
            choose = 'square spiral'
            turtle.reset()
            square_spiral(500)
        elif choose.lower() == 'cursor' or choose == '7':
            choose = 'cursor'
            turtle.reset()
            cursor(500)
        elif choose.lower() == 'star' or choose == '8':
            choose = 'star'
            turtle.reset()
            star(500)
        elif choose.lower() == 'duck' or choose == '9':
            choose = 'duck'
            turtle.reset()
            duck()
        elif choose.lower() == 'settings' or choose.lower() == 's':
            settings_choose = ''
            while settings_choose != '0' or settings_choose != 'exit':
                system("cls" if name == 'nt' else 'clear')
                settings_choose = input('+----------------------------+\n'
                                        '|          Settings          |\n'
                                        '| 1. Change pen color        |\n'
                                        '| 2. Change pen speed        |\n'
                                        '| 3. Change pen width        |\n'
                                        '| 0. Back to menu            |\n'
                                        '+----------------------------+')
                if settings_choose == '1':
                    COLOR = input('Available colors\n' + '\n'.join(colors))
        elif choose.lower() == 'exit' or choose == '0':
            print('Goodbye!')
            exit(0)
        else:
            print('Incorrect input!')


if __name__ == "__main__":
    menu()
