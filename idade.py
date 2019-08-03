def idade():
    # Converte o input em String 
    nome = str(input("Qual é o seu nome? "))
    # Converte o input em inteiro
    idade = int(input("Digite sua idade: "))

    if idade > 18:
        print("Ola,",nome," Você tem", idade,"anos. E é MAIOR de idade\n")
    else:
        print("Ola,", nome," Você tem", idade,"anos. E é MENOR de idade\n")

idade()

