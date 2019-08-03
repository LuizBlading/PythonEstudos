import turtle
t = turtle.Pen()

def desenharEstrela(numDeVezes, tam, angulo):
    for x in range(numDeVezes):
        t.forward(tam)
        t.left(angulo)

desenharEstrela(7, 100, 150)
