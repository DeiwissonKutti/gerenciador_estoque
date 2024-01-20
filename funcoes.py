from save import carregar_estoque, salvar_estoque

estoque = carregar_estoque()

def adicionar_produto(codigo, nome, valor_produto, quantidade, peso, descricao):
    if codigo in estoque:
        print("Produto já existe no estoque. Use a função de atualização se necessário.")
    else:
        estoque[codigo] = {'nome': nome, 'quantidade': quantidade, 'valor_produto': valor_produto, 'peso': peso, 'descricao': descricao}
        print(f"Produto '{nome}' adiciomado ao estoque.")

def atualizar_quantidade(codigo, nova_quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] = nova_quantidade
        print(f"Quantidade do produto '{estoque[codigo]['nome']}' atualizada para {nova_quantidade}.")
    else:
        print("Produto não encontrado no estoque.")

def exibir_estoque():
    print("Estoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

def salvar():
    salvar_estoque(estoque)