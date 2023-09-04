"""Consideraçoes importantes
    Foi utilizado a lista disponibilizada no blackboard do jogo da forca,
    o programa só vai rodar caso esteja salvo em um diretorio com esse arquivo.

    O arquivo contém palavras com acento, nao consegui indicativo pra quando a palavra tiver acentuacao,
    afim de teste, é possivel tirar o comentario do 'print(palavra_sorteada)' para ver qual é a palavra.

    Nao consegui utilizar cores no idle por conta disso a formatação ficou diferente
    do jogo original. Quando a pessoa acerta a letra na posicao correta ela fica
    maiuscula, quando acerta a letra mas a posição esta errada, é apontada uma 'flecha'(<<)
    e quando a letra nao esta na palavra é impresso normal em minusculo
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
