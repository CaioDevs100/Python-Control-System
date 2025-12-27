


import os

# Dicionário para armazenar os produtos do estoque 

banco_dados = {} 



# Função para excluir um produto do estoque
def excluir_produto():
    visualizar_estoque()
    nome = input("Nome do produto para excluir: ")
    if nome in banco_dados:
        del banco_dados[nome]
        print(" Produto excluído com sucesso!")
    else:
        print(" Produto não encontrado.")


# Função para atualizar os dados de um produto no estoque
def atualizar_produto():
    visualizar_estoque()
    if not banco_dados:
        print(" Estoque vazio.")
        return
    produto = input("Nome do produto a ser atualizado: ")
    banco_dados.pop(produto)
    novo_nome = input("Digite o novo produto: ")
    banco_dados[novo_nome] = {
        "preco": float(input("Digite o novo preço do produto: ")),
        "quantidade": int(input("Digite a nova quantidade em estoque: "))
    }


# Função para visualizar o estoque atual
def visualizar_estoque():
    if not banco_dados:
        print(" Estoque vazio.")
    else:
        print("<----> ESTOQUE ATUAL <---->")
        for produto, dados in banco_dados.items():
            print(f"Produto: {produto}")
            print(f"Preço: R$ {dados['preco']}")
            print(f"Quantidade: {dados['quantidade']}")
            print("----------------------")


# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    produto_name = input("Nome do produto: ")
    produto_preco = float(input("Preço do produto: "))
    quantidade_estoque = int(input("Quantidade em estoque: "))
    banco_dados[produto_name] = {'preco': produto_preco, 'quantidade': quantidade_estoque}
    print("Produto adicionado!")


# Função para limpar a tela tanto no Windows quanto no Linux/Mac
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar ():
    input("Pressione Enter para continuar...")


# Função para selecionar a opção do menu
def selecionar_opcao(opcao):
    if opcao == "1":
       adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        visualizar_estoque()
    elif opcao == "0":
        print("Saindo do Sistema...")
        exit()
    else:
        print("opcao invalida, tente novamente.")
    pausar()


# Função para exibir o menu e selecionar uma opcões do sistema
def exibir_menu():
    limpar_tela()
    print("------> MENU <------")
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Excluir Produto")
    print("4 - Visualizar Estoque")
    print("0 - Sair do Sistema")


# Função principal para iniciar o sistema
def iniciar_sistema():
    exibir_menu()
    opcao_escolhida = input("Selecione uma opcao: ")
    selecionar_opcao (opcao_escolhida)
    iniciar_sistema()

iniciar_sistema()