import forca
import adivinhacao

print("********************")
print("Escolhe o seu jogo!")
print("********************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual Jogo? "))

if jogo == 1:
    print("Jogando da forca")
    forca.jogar_forca()
elif jogo == 2:
    print("Jogando de adivinhação")
    adivinhacao.jogar_adivinhacao()