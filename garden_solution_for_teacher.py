# Готовий розв'язок уроку 2 — для вчителя.
# Демонструє основне завдання + усі додаткові експерименти.
# УЧНЯМ НЕ ДАВАТИ.

from turtle import *
from random import random

speed(0)


def draw_flower(x, y, petal_color="red"):
    """Малює одну квітку у точці (x, y) з заданим кольором пелюсток."""
    penup()
    goto(x, y - 280)
    setheading(90)
    pendown()

    # стебло і листочки
    color("green")
    forward(60)
    circle(20)
    forward(60)
    right(180)
    circle(20)
    right(180)
    forward(60)
    circle(20)
    forward(100)

    # пелюстки
    right(90)
    color(petal_color)
    for i in range(6):
        circle(25)
        left(60)

    # серединка
    penup()
    goto(x, y - 10)
    color("yellow")
    pendown()
    circle(10)


# === Основне завдання: сад 3×5 ===
COLORS = ["red", "orange", "yellow", "purple", "pink"]

for row in range(3):
    for col in range(5):
        x = -200 + col * 100
        y = -150 + row * 150

        # варіант 1: всі однакові
        # draw_flower(x, y)

        # варіант 2: кожен ряд свого кольору
        # draw_flower(x, y, COLORS[row])

        # варіант 3: випадковий колір RGB
        draw_flower(x, y, (random(), random(), random()))


done()
