import random

#cria uma lista de palavras que serão sorteadas
palavras = ["python", "linguagem", "logica", "programacao"]

#Escolhemos uma das palavras 
palavras_sorteada = random.choice(palavras)
print(palavras_sorteada)

#Criamos uma string com traços para representar as letras 
palavra_oculta = "||" * len(palavras_sorteada)
print(palavra_oculta)

#Criamos uma lista para armazenar as letras que ja foram falads
letras_adivinhadas = []
max_tentativas = 6 

while True:
    #Mostra na tela palavra escondida
    print(palavra_oculta)

    #Pedimos para o jogador digitar uma letra
    letra = input("Digite uma letra: ")

    #Verificamos se a letra ja foi digitada
    if letra in letras_adivinhadas:
        print("Você já digitou essa letra. Tente outra. ")
        continue #Essa função faz com que o programa volte para o inicio do loop while

    #Adicionamos a letra a letra de letras digitadas 
    letras_adivinhadas.append(letra)