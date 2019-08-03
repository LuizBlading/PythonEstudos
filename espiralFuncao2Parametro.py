# Espiral com Função 2

import turtle
import random

t = turtle.Pen()

def desenharCirculo(numDeVezes, giro):
    for i in range(numDeVezes):
        t.circle(100)
        t.left(giro)

desenharCirculo(32, 61)
