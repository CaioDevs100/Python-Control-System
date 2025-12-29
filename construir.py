

# Importa o módulo OS para operações do sistema operacional
import os 

# Dicionário para armazenar os produtos do estoque 

banco_dados = {} 
vendas = []


def visualizar_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    print("<----> HISTÓRICO DE VENDAS <---->")
    for i, venda in enumerate(vendas, start=1):
        print(f"Venda {i}")
        print(f"Cliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Total: R$ {venda['total']:.2f}")
        print("------------------------------")


# Função para registrar uma venda
def registrar_venda():
    if not banco_dados:
        print("Estoque vazio. Não é possível vender.")
        return

    visualizar_estoque()

    produto = input("Nome do produto vendido: ")

    if produto not in banco_dados:
        print("Produto não encontrado.")
        return

    quantidade_vendida = int(input("Quantidade vendida: "))

    if quantidade_vendida > banco_dados[produto]["quantidade"]:
        print("Quantidade insuficiente em estoque.")
        return

    cliente = input("Nome do cliente: ")

    total = quantidade_vendida * banco_dados[produto]["preco"]

    # Atualiza estoque
    banco_dados[produto]["quantidade"] -= quantidade_vendida

    # Registra venda
    venda = {
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade_vendida,
        "total": total
    }

    vendas.append(venda)

    print("Venda registrada com sucesso!")
    print(f"Total da venda: R$ {total:.2f}")


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
        visualizar_estoque
        return

    produto = input("Nome do produto a ser atualizado: ")

    if produto not in banco_dados:
        print(" Produto não encontrado.")
        return

    # Validação do novo nome
    novo_nome = input("Digite o novo nome do produto: ")
    if novo_nome == "":
        print(" O nome não pode ser vazio.")
        return

    # Validação do preço
    while True:
        preco_input = input("Digite o novo preço do produto: ")
        try:
            preco = float(preco_input)
            break
        except ValueError:
            print(" Digite um valor numérico válido para o preço.")

    # Validação da quantidade
    while True:
        quantidade_input = input("Digite a nova quantidade em estoque: ")
        try:
            quantidade = int(quantidade_input)
            break
        except ValueError:
            print(" Digite um número inteiro válido para a quantidade.")

    # Atualiza o produto com segurança
    banco_dados[produto]["preco"] = preco
    banco_dados[produto]["quantidade"] = quantidade
    if novo_nome != produto:
        banco_dados[novo_nome] = banco_dados.pop(produto)
    

    print(" Produto atualizado com sucesso!")



# Função para visualizar o estoque atual
def visualizar_estoque():
    if not banco_dados:
        print(" Estoque vazio.")
    else:
        print("<----> ESTOQUE ATUAL <---->")
        for produto, dados in banco_dados.items():
            print(f"Produto: {produto}")
            print(f"Preço: R$ {dados['preco']:.2f}")
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
    elif opcao == "5":
        registrar_venda()
    elif opcao == "6":
        visualizar_vendas()
    elif opcao == "0":
        print("Saindo do Sistema...")
        exit()
    else:
        print("opcao invalida, tente novamente.")
    pausar()


# Função para exibir o menu e selecionar uma opcões do sistema
def exibir_menu():
    limpar_tela()
    print("<------> MENU <------>")
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Excluir Produto")
    print("4 - Visualizar Estoque")
    print("5 - Registrar Venda")
    print("6 - Visualizar Histórico de Vendas")
    print("0 - Sair do Sistema")


# Função principal para iniciar o sistema
def iniciar_sistema():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opcao: ")
        if opcao == "0":
            print("Saindo do sistema...")
            break
        selecionar_opcao(opcao)

iniciar_sistema()