# calculo de IMC

altura = float(input("Qual é a sua altura? "))
peso = float(input("Quanto você pesa? "))

#calculo do imc

imc = peso / (altura**2)

print("O seu IMC é: {:.2f}".format(imc))
                     
