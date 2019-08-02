from math import hypot

cOp = float(input("Comprimento do Cateto Oposto: "))
cAdj = float(input("Comprimento do Cateto Adjacente: "))

hip = hypot(cOp,cAdj)

print("A Hipotenusa é: {:.2f}".format(hip))
