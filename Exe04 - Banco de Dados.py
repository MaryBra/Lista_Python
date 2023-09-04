
"""Estratégias Utilizadas:
O usuário define os campos obrigatórios para o cadastro.
O programa oferece opções para cadastrar usuários de forma personalizada.
Os usuários são armazenados em um banco de dados global.
É possível imprimir informações sobre os usuários com opções de filtragem."""

# Dicionário global para armazenar os usuarios
banco_usuarios = []

# Função para cadastrar um usuario fornecendo valores para os campos obrigatórios e opcionais
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    #Pede ao usuario que digite as informações com base nos campos obrigatorios escolhidos
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo {campo}: ")
        usuario[campo] = valor

    #Pergunta ao usuario se deseja adicionar mais campos, quais são e seus valores
    while True:
        campos_adicionais = input("Deseja adicionar mais campos? (Digite 'sair' para encerrar): ")
        if campos_adicionais.lower() == 'sair':
            break
        campo = input("Digite o nome do campo adicional: ")
        valor = input(f"Digite o valor para o campo {campo}: ")
        usuario[campo] = valor

    #Adiciona o elemento 'usuario' no dicionario global
    banco_usuarios.append(usuario)
    print("Usuario cadastrado com sucesso!")

# Função para imprimir usuarios com várias opções
#Passando como parametro: args (str): Nomes de usuários a serem filtrados (opcional).
#kwargs (dict): Opções de filtro, como campos e valores (opcional).
def imprimir_usuarios(*args, **kwargs):
    if not args:
        # Imprimir todos os usuarios com todas as informações
        for usuario in banco_usuarios:
            print(usuario)
    else:
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()) and (
                    not args or usuario.get("nome") in args):
                print(usuario)


#Variavel que pede os campos obrigatorios ao usuario no inicio do programa
campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(",")

#Loop menu principal
while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")
    print("0 - Encerrar")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        #Chama a função cadastrar_usuario passando os cmapos obrigatórios
        cadastrar_usuario(campos_obrigatorios)
    elif opcao == "2":
        #Abre um menu de busca
        menu_busca = input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nDigite a opção desejada: ")
        if menu_busca == "1":
            #Chama a função que imprime os usuarios sem filtro(imprime todos)
            imprimir_usuarios()
        elif menu_busca == "2":
            #Imprime os usuarios buscados pelos nomes
            nomes = input("Digite os nomes dos usuários separados por vírgula: ").split(",")
            imprimir_usuarios(nomes=nomes)
        elif menu_busca == "3":
            #Imprime os usuarios buscados pelos campos e valores
            campos = input("Digite os nomes dos campos separados por vírgula: ").split(",")
            valor = input("Digite o valor para os campos: ")
            imprimir_usuarios(campos=campos, valor=valor)
        elif menu_busca == "4":
            #Imprime os usuarios buscados pelo nome, cmapo e valor
            nomes = input("Digite os nomes dos usuarios separados por vírgula: ").split(",")
            campos = input("Digite os nomes dos campos separados por vírgula: ").split(",")
            valor = input("Digite o valor para os campos: ")
            imprimir_usuarios(nomes=nomes, campos=campos, valor=valor)
    elif opcao == "0":
        break
