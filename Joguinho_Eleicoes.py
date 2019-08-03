import emoji

print("Olá, seja bem vindo! \n\nVamos jogar?")

sim = "s"
nao = "n"

# Numeros dos candidatos
CiroGomes = 12
Haddad = 13
Bolsonaro = 17
Alckmin = 45


tecla = str(input("Tecle 's' para SIM, e 'n' para NÃO: \n"))

def continuar():
    tecla = str(input("Tecle 'P' para voltar a votação: \n"))

    if (tecla == 'c'):
        jogando = True
    else:
        jogando = False
    pass

def imprimeCandidatos():
    #Imprime os resultados dos candidatos
    print("O Candidato", candidatos[0], "tem {} votos!\n".format(vCiro))
    print("O Candidato", candidatos[1], "tem {} votos!\n".format(vHaddad))
    print("O Candidato", candidatos[2], "tem {} votos!\n".format(vBolsonaro))
    print("O Candidato", candidatos[3], "tem {} votos!\n".format(vAlckmin))


if(tecla == "s"):
    print("Legal, vamos jogar!" , emoji.emojize(" :smile:", use_aliases=True))

    #Iniciação do Jogo
    jogando = True
    vCiro = 0
    vHaddad = 0
    vBolsonaro = 0
    vAlckmin = 0

    while jogando:

        sair = ""
        if (sair == "q"):
            jogando = False #Fecha o jogo

        #Regra do jogo
        print("Que o questionário comece! \nPara sair do jogo, tecle 'q'\n")

        #Inicio das perguntas
        print("Em 2018 teremos as eleições para presidente,"
              "na sua opinião, quem deve ganhar?")

        #Lista de candidatos
        candidatos = ["Ciro Gomes", "Haddad", "Bolsonaro", "Alckmin"]

        #Opções para o usuario
        op = int(input("Digite o número do seu candidato\n"
                       "Ciro Gomes - 12\nHaddad - 13\nBolsonaro - 17\nAlckmin - 45\n"))

        print("=======================================================")

        #Escolha das opções dos candidatos
        if (op == CiroGomes):
            vCiro += 1
            imprimeCandidatos()
            continuar()

        elif (op == Haddad):
            vHaddad += 1
            imprimeCandidatos()
            continuar()

        elif (op == Bolsonaro):
            vBolsonaro += 1
            imprimeCandidatos()
            continuar()

        elif (op == Alckmin):
            vAlckmin += 1
            imprimeCandidatos()
            continuar()
else:
    print("Ok, nos vemos na próxima!")