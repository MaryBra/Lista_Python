"""
Estratégias Utilizadas:
Este é um jogo da velha estendido em um tabuleiro 4x4.
A função 'imprime_tabuleiro' exibe o estado atual do tabuleiro após cada jogada.
A função 'verifica_tabuleiro' verifica se um jogador venceu em alguma linha, coluna ou diagonal.
O jogo continua até que um jogador vença ou ocorra um empate (deu velha).
O tabuleiro é representado como uma lista 't' de 16 elementos, onde '_' indica uma posição vazia.
O jogo é jogado em um tabuleiro 4x4, e as posições são numeradas de 1 a 16."""


#Funcao que imprime o tabuleiro
def imprime_tabuleiro(t):
    for indice in range(len(t)):
        print(t[indice], end=" | ")
        if indice == 3 or indice == 7 or indice == 11 or indice == 15:
            print("")

#Função que verifica o estado do jogo 
def verifica_tabuleiro(t, jogador):
    #Passando as linhas, colunas e diagonais para verificar se houve um vencedor
    linhas = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    colunas = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
    diagonais = [[0, 5, 10, 15], [12, 9, 6, 3]]
    
    for linha in linhas + colunas + diagonais:
        #Utilizando a funcao 'all' para verificar se todos os elementos satisfazem a condição
        if all(t[i] == jogador for i in linha):
            return 1 if jogador == 'x' else 2
    #Retorna 0 caso tenha dado empate
    return 0

#Tela inicial
print("Você precisa escolher uma posição no tabuleiro para marcar sua jogada, de acordo com a numeração:")
print("1  2  3  4\n5  6  7  8\n9  10 11 12\n13 14 15 16")

#Variavel que conta a quantidade de jogadas 
qntd_jogadas = 0
#Criaçao do 'tabuleiro'(lista) com 16 elementos
t = ["_"] * 16

#Loop principal
while True:
    #Variavel jogador determina de quem é a vez de jogar, se a jogada for par é o 'x' e se for impar é o 'o'
    jogador = 'x' if qntd_jogadas % 2 == 0 else 'o'
    escolha = int(input(f"\nVez do '{jogador}'\nEscolha uma posição: "))

    #Loop que verifica se a jogada é valida
    while t[escolha - 1] != "_":
        print("Sua escolha foi inválida! Veja como está o jogo:")
        imprime_tabuleiro(t)
        escolha = int(input(f"\nVez do '{jogador}'\nEscolha uma posição: "))

    #Inclui o valor escolhido na variavel t (- 1 pq começa em 0)
    t[escolha - 1] = jogador
    qntd_jogadas += 1

    vencedor = verifica_tabuleiro(t, jogador)

    #Condição que verifica se existe um vencedor ou se o numero de jogadas chegou ao limite
    if vencedor or qntd_jogadas == 16:
        break

    imprime_tabuleiro(t)
#printa a mensagem final
if vencedor:
    print(f"Parabéns! '{jogador}' ganhou!")
else:
    print("Deu velha! Empatou :(")

imprime_tabuleiro(t)
