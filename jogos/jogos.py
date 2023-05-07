import forca
import adivinhacao

def escolhe_jogo():
    print("="*18)
    print("Escolha seu Jogo")
    print("="*18)

    jogo = int(input("\nQual jogo você deseja jogar ? \n (1) Forca (2) Adivinhação\n"))

    if(jogo == 1):
        print("\nJogando Forca\n")
        forca.jogar()
    elif(jogo == 2):
        print("\nJogando Adivinhação\n")
        adivinhacao.jogar()
    
if(__name__ == "__main__"):
    escolhe_jogo()