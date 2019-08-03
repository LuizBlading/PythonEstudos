#quadrado.py - desenha um quadrado colorido na tela com o fundo preto

import turtle
t = turtle.Pen()
turtle.bgcolor("Black")
t.pencolor("white")

for x in range(1000):
    t.forward(x)
    t.left(90)
