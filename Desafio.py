# Desafio.py

import turtle

t = turtle.Pen()

t.pencolor("red") # Coloco a cor vermelha para a turtle

def desenharQuadrado(tamanhoLinha): # Crio uma função com parametro para definir o tamanho da linha
    for repeticao in range(4): #Quantidade de vezes que irá se repetir
        t.forward(tamanhoLinha) # Anda para frente com o valor que a pessoa/usuario digitou
        t.left(90) # Gira 90° (graus) para a esquerda

desenharQuadrado(120) #Chama a função passando o valor de 120 que será a quantidade que a turtle vai andar
