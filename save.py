import json

def carregar_estoque():
    try:
        with open('estoque.json','r' ) as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    

def salvar_estoque(estoque):
    with open('estoque.json','w') as arquivo:
        json.dump(estoque, arquivo, indent=2)