"""Consideraçoes importantes
    Foi utilizado a lista disponibilizada no blackboard do jogo da forca,
    o programa só vai rodar caso esteja salvo em um diretorio com esse arquivo.

    O arquivo contém palavras com acento, não consegui indicativo pra quando a palavra possuir acentuação.
    
    Afim de teste, é possivel tirar o comentario do 'print(palavra_sorteada)' para ver qual é a palavra(linha 45).

   Estratégias Utilizadas:
    Este é um jogo que desafia o jogador a adivinhar uma palavra de acordo com o número de letras especificado.
    O jogo utiliza um arquivo de texto ("lista_palavras.txt") para carregar um conjunto de palavras determinado.
    O jogador tem 6 chances para adivinhar a palavra correta, assim como no jogo original.
    Durante cada tentativa, o programa fornece dicas sobre as letras corretas e na posição correta (em maiúsculo) e letras corretas mas na posição errada (com '<<' ao lado).
    O jogo termina quando o jogador adivinha a palavra ou esgota todas as chances.
    O jogador especifica o número de letras da palavra a ser adivinhada.
    O programa seleciona aleatoriamente uma palavra da lista com o número correto de letras usando o módulo 'random'.


"""

import random

#variavel com o endereço do arquivo .txt (mesmo utilizado no jogo da forca)
arquivo = "lista_palavras.txt"

#Funcao que le o cada string do arquivo
def le_arquivo(arq):
    with open("lista_palavras.txt", encoding = "UTF-8") as f:
        return [linha.strip() for linha in f]

#Chamando a funcao e passando o endereço como parametro
lista = le_arquivo(arquivo)

#lista que vai selecionar somente as palavras que possuem o numero de letras determinado pelo usuario 
lista_nova = []

numero = int(input("Digite o numero de letras da palavra: "))
for item in lista:
    #verifica quais sao as palavras que possuem n letras e as coloca em uma nova lista
    if len(item) == numero:
        lista_nova.append(item)
        #sorteia uma palavra a partir da lista nova
        palavra = random.randint(0, len(lista_nova)-1)
palavra_sorteada = lista_nova[palavra]
#print(palavra_sorteada)

#loop que se encerra quando as chances acabarem(6 chances)
for chances in range(6):
    escolha = input(f"\nDigite uma palavra com {numero} letras:").lower()

    #Loop que verifica se as letras estao certas
    for i in range(min(len(escolha), numero)):
        #Se a letra escolhida estiver na palavra e na posição correta, sera escrita em maiusculo
        if escolha[i] == palavra_sorteada[i]:
            acerto = escolha[i].upper()
            print(acerto, end =" ")
        #Se a letra estiver na palavra mas na posição errada será impressa como "letra<< "
        elif escolha[i] in palavra_sorteada:
            print(escolha[i].upper(), end = "<< ")
        #Se a letra nao estiver na palavra, sera impresso normal 
        else:
            print(escolha[i], end = " ")
    
    #Se o usuario acertar a palavra será impresso a seguinte mensagem:
    if escolha == palavra_sorteada:
        print(f"\nParabens, voce acertou! A palavra era {palavra_sorteada}")
        break
