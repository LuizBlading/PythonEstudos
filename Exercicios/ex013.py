# Script para calcular reajuste de salário de 15%

salario = float(input("Quanto é seu salário? "))
aumento_15 = (salario * 15)/100
novoSalario = salario + aumento_15

print("Seu salário vai passar de R${} para R${} com 15% de aumento (Valor em dinheiro: R${})!".format(salario, novoSalario, aumento_15))
