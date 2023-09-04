# Função para imprimir o tabuleiro
def imprime_tabuleiro(t):
    for row in t:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

# Função para verificar se um jogador venceu
def verifica_tabuleiro(t, jogador):
    n = len(t)
    linhas = [[(i, j) for j in range(n)] for i in range(n)] #lista de todas as linhas
    colunas = [[(i, j) for i in range(n)] for j in range(n)] # lista de todas as colunas
    diagonais = [[(i, i) for i in range(n)], [(i, n - 1 - i) for i in range(n)]]#lista das diagonais

    #Verifica se o jogador ganhou em alguma linha, coluna ou diagonal
    for linha in linhas + colunas + diagonais:
        if all(t[i][j] == jogador for i, j in linha):
            return True

    return False

#Variavel que define o tamanho do tabuleiro
n = int(input("Digite o tamanho da matriz n x n: "))
#Inicializa o tabuleiro como uma matriz vazia de tamanho n x n
t = [["_" for _ in range(n)] for _ in range(n)]

#Variavel que controla o numero de jogadas
qntd_jogadas = 0

#Loop principal
while True:
    jogador = 'x' if qntd_jogadas % 2 == 0 else 'o' #Alterna entra os jogadores 'x' e 'o'
    imprime_tabuleiro(t)

    #Variavel que recebe a lina e a coluna que o usuario vai jogar separados por 'espaço'
    escolha = input(f"\nVez do '{jogador}'\nEscolha uma posição (linha coluna): ").split()

    #Se a qntd de numeros digitados for diferente de dois ele repete o comando anterior
    if len(escolha) != 2:
        print("Entrada inválida! Digite a linha e a coluna separadas por espaço.")
        continue

    # Converte os elementos da lista 'escolha' em números e atribui a variável 'linha' o primeiro elemento e 'coluna' o segundo elemento
    linha, coluna = map(int, escolha)

    # Verifica se a escolha do usuario está fora dos limites do tabuleiro
    # ou se a posiçao ja esta ocupada
    if linha < 1 or linha > n or coluna < 1 or coluna > n or t[linha - 1][coluna - 1] != "_":
        print("Escolha inválida! Tente novamente.")
        continue

    t[linha - 1][coluna - 1] = jogador
    qntd_jogadas += 1

    #Se a funcao retorna True, é impresso a mensagem final e o jogo acaba
    if verifica_tabuleiro(t, jogador):
        imprime_tabuleiro(t)
        print(f"Parabéns! '{jogador}' ganhou!")
        break

    #Se a quantidade de jogadas excede é exibido a mensagem de empate
    if qntd_jogadas == n * n:
        imprime_tabuleiro(t)
        print("Deu velha! Empatou :(")
        break
