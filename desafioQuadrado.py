import turtle

t = turtle.Pen()

def desenhaQuadrado(tamanhoDaLinha):
    for x in range(tamanhoDaLinha):
        t.forward(x) #Vai de 0 até o valor da variavel como parametro.
                        # e Essa é a quantidade que irá andar
        t.left(90) #vira para a esquerda

desenhaQuadrado(150)
