def recomecar():
    c = str(input("\nDigite 'c' para começar de novo: "))
    if c == 'c':
        num_primo()

def num_primo():
    num = int(input("Digite um número para sabermos se é primo: "))

    for n in range(2,num):
        if (num % n) == 0:
            print("Não é primo!")
            recomecar()
            break
        else:
            print("É primo!")
            recomecar()
            break

num_primo()

