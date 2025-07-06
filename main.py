print("Bem-vindo(a) ao sistema de gerenciamento de livros!")
print("Desenvolvido por: Thalita Vitória de Freitas\n")

# Lista onde os livros serão armazenados (lista de dicionários)
lista_livro = []

# Variável para controle automático do ID dos livros
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id):
    print("\n=== Cadastro de Livro ===")

    # Entrada e conversão do ID para inteiro
    try:
        id = int(input("Digite o ID do livro: "))
    except ValueError:
        print("ID inválido! Use apenas números.")
        return

    nome = input("Nome do livro: ")
    autor = input("Autor do livro: ")
    editora = input("Editora do livro: ")

    # Cria dicionário com os dados do livro
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }

    # Adiciona o dicionário à lista principal
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")


# Função para consultar livros
def consultar_livro():
    while True:
        print("\n=== Consultar Livro ===")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Todos os Livros ---")
            for livro in lista_livro:
                print(livro)

        elif opcao == "2":
            try:
                id_consulta = int(input("Digite o ID do livro: "))
                for livro in lista_livro:
                    if livro["id"] == id_consulta:
                        print(livro)
                        break
                else:
                    print("Livro não encontrado.")
            except:
                print("Entrada inválida.")

        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrados = False
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower():
                    print(livro)
                    encontrados = True
            if not encontrados:
                print("Nenhum livro encontrado para este autor.")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

# Função para remover livro pelo ID
def remover_livro():
    try:
        id_remove = int(input("Digite o ID do livro a ser removido: "))
        for livro in lista_livro:
            if livro["id"] == id_remove:
                lista_livro.remove(livro)
                print("Livro removido com sucesso.")
                return
        print("ID inválido. Livro não encontrado.")
    except:
        print("Entrada inválida.")

# Estrutura principal do programa com menu de opções
while True:
    print("\n=== Menu Principal ===")
    print("1. Cadastrar Livro")
    print("2. Consultar todos")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)

    elif escolha == "2":
        consultar_livro()

    elif escolha == "3":
        remover_livro()

    elif escolha == "4":
        print("Encerrando programa... Até logo!")
        break

    else:
        print("Opção inválida!")
