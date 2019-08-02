nome = str(input("Digite o seu nome: "))

print("\nAnalisando o seu nome...\n")
print("O seu nome é: {}\n".format(nome))

print("O seu nome em MAIUSCULO é: {}".format(nome.upper())) #MAIUSCULAS
print("O seu nome em MINUSCULO é: {}".format(nome.lower()))#MINUSCULAS
print("\n")


# Resposta Minha
qFrase1 = nome.split()
novaFrase = qFrase1[0] + qFrase1[1]
print(len(novaFrase))


#Resposta Minha
print("\nParte 4\n")
qFrase2 = nome.split()
print(qFrase2)
print(len(qFrase2[0]))

