# Espiral.py

import turtle

t = turtle.Pen()

velocidade = "fastest" # Variavel que define a velocidade
t.speed(velocidade) # da a velocidade para a turtle

for x in range(100):
    t.circle(x)
    t.left(91)
