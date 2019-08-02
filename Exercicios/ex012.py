preco = float(input("Qual o preço do produto? R$"))
desconto = ((preco * 5)/100)
#Outra maneira de fazer a conta
novo = preco - (preco * 5/100)
print("Jeito LUIZ:\nO desconto de 5% é de {:.2f} e o preço total ficou de {:.2f}".format(desconto, (preco - desconto)))
#print("O produto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}".format(desconto, (preco - desconto)))
print("\n\nJeito GUANABARA:\nO produto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}".format(preco, novo))