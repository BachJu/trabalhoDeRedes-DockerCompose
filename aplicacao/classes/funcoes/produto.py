from classes.bd.produto import Produto

def criar_produto(nome, preco, quantidade):
    p = Produto()
    p.set_nome(nome)
    p.set_preco(preco)
    p.set_quantidade(quantidade)
    p.inserir_produto()

def listar_produtos():
    p = Produto()
    return p.recuperar_produtos()

def atualizar_produto(id_produto, nome, preco, quantidade):
    p = Produto()
    p.set_id(id_produto)
    p.set_nome(nome)
    p.set_preco(preco)
    p.set_quantidade(quantidade)
    p.atualizar_produto()

def deletar_produto(id_produto):
    p = Produto()
    p.set_id(id_produto)
    p.deletar_produto()

def buscar_produto_por_id(id_produto):
    p = Produto()
    p.set_id(id_produto)
    return p.recuperar_dados()