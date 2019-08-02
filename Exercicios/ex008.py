'''
    Ler valor em Metros e converter
    em centimetros e milimetros
'''

valor = int(input("Digite um valor em metros: "))
centimetro = 100
milimitro = 1000

vCenti = valor * centimetro
vMili = valor * milimitro

print(valor, "Metros fica: {}".format(vCenti), "Centimetros\n E Milimetros é: {}".format(vMili))