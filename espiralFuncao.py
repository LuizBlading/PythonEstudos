# Espiral com função

import turtle


t = turtle.Pen()

def desenhaCirculo():
    t.circle(100)
    t.left(90)

for i in range(4):
    desenhaCirculo()
