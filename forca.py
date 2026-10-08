import random

#cria uma lista de palavras que serão sorteadas
palavras = ["python", "linguagem", "logica", "programacao"]

#Escolhemos uma das palavras 
palavras_sorteada = random.choice(palavras)
print(palavras_sorteada)

#Criamos uma string com traços para representar as letras 
palavra_oculta = "**" * len(palavras_sorteada)

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

    #Verificamos se a letra digitada está na palavra sorteada
    if letra in palavras_sorteada:
        lista = []
        for indice in range(len(palavras_sorteada)):
            if letra == palavras_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_oculta[indice])
        palavra_oculta = ''.join(lista)
    else:
        max_tentativas -= 1 
        print(f'Letra não encontrada. Você tem {max_tentativas} tentativas restantes. ')

    #Verificamos se o jogador ganhou ou perdeu
    if palavra_oculta == palavras_sorteada:
        print(f'Parabéns! Você ganhou! A palavra era {palavras_sorteada}.')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu! A palavra era {palavras_sorteada}.')
        break
        