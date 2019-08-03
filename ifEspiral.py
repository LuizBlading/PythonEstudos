#Espiral com função

import turtle

t =  turtle.Pen()

resposta = str(input("Você quer ver meu desenho? SIM ou NÃO? "))

if resposta == "sim":
    print("Carregando...")
    t.width(2)

    for x in range(100):
        t.forward(x*2)
        t.left(89)
    print("Ok, terminei de desenhar!")
