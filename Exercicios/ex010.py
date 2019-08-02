'''
    Programa para saber quanto
    tem em dinehiro e converter
    em dolares para comprar
'''

#Dinheiro da pessoa
dinheiro = float(input("Quanto dinheiro você tem? "))
#Valor do dolar
dolar = 3.27

#Conversão de reais para dolar
conversao = (dinheiro / dolar)

print("Você pode comprar: US${:.2f}".format(conversao))
