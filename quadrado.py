# quadrado.py - desenha um quadrado colorido na tela com o fundo preto
# Esta linha vermelha com o sinal # é um comentário
# Comentários são úteis para você anotar o que o programa faz

import turtle # Importa a tartaruga para o programa usar
t = turtle.Pen() # salva a função Pen() dentro da variavel t
turtle.bgcolor("black") #Chama a função que desenha a cor do fundo
CorDaLinha = "red" #Variavel para guardar o nome da cor da linha

t.pencolor(CorDaLinha) #Muda a cor da linha
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
