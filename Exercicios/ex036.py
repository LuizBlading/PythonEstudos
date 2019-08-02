valorDaCasa = int(input("Qual o valor da casa? R$"))
salario = int(input("Qual é o seu salário? R$"))
qntParcelas = int(input("Em quantos anos quer pagar? "))

valorPrestacao = valorDaCasa/(qntParcelas * 12)
minimo = salario * 30 / 100

if valorPrestacao > (minimo):
    print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}. \n Empréstimo NEGADO!"
          .format(valorDaCasa, qntParcelas, valorPrestacao))
else:
    print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}. \n Empréstimo CONCEDIDO!"
          .format(valorDaCasa, qntParcelas, valorPrestacao))
