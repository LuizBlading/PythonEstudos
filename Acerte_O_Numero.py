'''
Created on 1 de ago de 2018

@author: luiz Felipe
'''

import random 

numero = random.randint(1, 100);

tentativas = 0
escolha = 0

while escolha != numero:
    escolha = int(input("Informe um número entre 1 e 100: "))
    tentativas += 1
    if (escolha > numero):
        print("O número", escolha,"é Maior que o número que sorteei! \n")
    
    elif (escolha < numero):
        print("O número", escolha,"é Menor que o número que sorteei! \n")
        
print("Acertou! O número sorteado era: {}".format(numero))
print("Você usou {} tentativas\n".format(tentativas))