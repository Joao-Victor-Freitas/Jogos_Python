import random

def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letra_certa(palavra):
    return ["_" for letra in palavra]


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencendor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perderdor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chutes(palavra_certa, letra_certa):
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print("Jogando...\n")

        chute = input("Qual a letra?\n").strip().upper()

        if(chute in palavra_certa):
            index = 0
            for letra in palavra_certa:
                if(chute == letra.upper()):
                     letra_certa[index] = letra
                index += 1
        else:
            erros += 1 
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in  letra_certa
        print( letra_certa)

    if(acertou):
        mensagem_vencendor()

    else:
        mensagem_perderdor(palavra_certa)

    print("Fim de Jogo")


def jogar():

    imprime_abertura()

    palavra_secreta = carrega_palavra()

    letras_acertadas = inicializa_letra_certa(palavra_secreta)

    print( letras_acertadas)

    marca_chutes(palavra_secreta, letras_acertadas)

if(__name__ == "__main__"):
    jogar()