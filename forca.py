import random

#cria uma lista de palavras que serão sorteadas
palavras = ["python", "linguagem", "logica", "programacao"]

#Escolhemos uma das palavras 
palavras_sorteada = random.choice(palavras)
print(palavras_sorteada)

#Criamos uma string com traços para representar as letras 
palavra_oculta = "||" * len(palavras_sorteada)
print(palavra_oculta)