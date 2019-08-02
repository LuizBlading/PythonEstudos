km = float(input("Quantos km rodados? "))
dias = int(input("Quantos dias alugados? "))

pDia = 60
pKM = 0.15

precoTotal = (dias * pDia) + (km * pKM)

print("O total a pagar é de R${:.2f}".format(precoTotal))
