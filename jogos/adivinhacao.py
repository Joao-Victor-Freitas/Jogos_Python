from random import randrange

def jogar():

    print("="*33)
    print("Bem vindo ao jogo da Advinhação!")
    print("="*33)

    numero_secreto = randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?\n")

    print("(1) Fácil (2) Médio (3) Difícil\n")

    dificuldade = int(input())
    print("\n")

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1) :
        print("Tentativa {} de {}\n".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100! Tente novamente")
            continue

        if(numero_secreto == chute):
            print("Você acertou! Parabéns\n")
            print(f"Total de Pontos foi de {pontos}")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto.\n")
                
            elif(chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            

    if(rodada == total_de_tentativas and chute != numero_secreto):
        print(f"Número de tentativas esgotado! O número secreto era {numero_secreto}.\n")

if(__name__ == "__main__"):
    jogar()