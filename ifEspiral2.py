# Espiral com função e INPUT

import turtle

t= turtle.Pen()

resposta = str(input("Você quer ver o meu desenho? \nDigite 'sim' para SIM ou 'nao' para NÃO? -> ")) #Pede informação para a pessoa

if resposta == "sim": # Verifica se digitou sim
    print("Carregando...")
    t.width(2) # Faz com que a largura da turtle seja 2

    for x in range(100): # Repete de 0 a 100 os passos da linha de baixo
        t.forward(x*2) # Anda o valor atual de x * 2 ( Ou seja, x vezes 2 )
        t.left(89) # Vira para a esquerda em 89 graus

    print("Ok, terminei de desenhar!") # Depois que terminar de desenhar, escreve essa mensagem na tela.
