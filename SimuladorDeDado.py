#Simulador de Dado
#Objetivo: O script deve gerar um valor aleatório entre 1 e 6 e permitir que o usuário rode o script
#quantas vezes quiser até que a resposta seja "não".
import random

resposta = str(input("Você gostaria de jogar o dado? Digite 'SIM' OU 'NÃO': ")).upper()

while resposta != "SIM":
    resposta = str(input("Você gostaria de jogar o dado? Digite 'SIM' OU 'NÃO': ")).upper()
    while resposta == "SIM":
        x = random.randint(1, 6)
        print(x)
        resposta = str(input("Jogar o dado novamente? Digite 'SIM' OU 'NÃO': ")).upper()
    if resposta == "NÃO":
        break