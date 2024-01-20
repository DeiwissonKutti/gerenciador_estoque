from funcoes import adicionar_produto, atualizar_quantidade, exibir_estoque, salvar

while True:
    print("\n### Controle de Estoque ###")
    print("1 - Adicionar produto")
    print("2 - Atualizar Quantidade")
    print("3 - Exibir Estoque")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == str(1):
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        valor_produto = input("Valor do produto: ")
        quantidade = input("Quantidade do produto: ")
        peso = input("Peso do produto: ")
        descricao = input("Descrição do produto do produto: ")

        adicionar_produto(codigo, nome, valor_produto, quantidade, peso, descricao)
        salvar()
    elif escolha == str(2):
        codigo = input("Código do produto do produto: ")
        quantidade = input("Quantidade atual do produto do produto: ")
        atualizar_quantidade(codigo, quantidade)
        salvar()
    elif escolha == str(3):
        exibir_estoque()
    elif escolha == str(4):
        salvar()
        break