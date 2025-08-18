from aplicacao.classes.bd.venda import Venda

def criar_venda(data, status, id_funcionario):
    v = Venda()
    v.set_data(data)
    v.set_status(status)
    v.set_IdFuncionario(id_funcionario)
    v.inserir_venda()

def listar_vendas():
    v = Venda()
    return v.recuperar_vendas()

def atualizar_venda(id_venda, data, status, id_funcionario):
    v = Venda()
    v.set_id(id_venda)
    v.set_data(data)
    v.set_status(status)
    v.set_IdFuncionario(id_funcionario)
    v.atualizar_venda()

def deletar_venda(id_venda):
    v = Venda()
    v.set_id(id_venda)
    v.deletar_venda()

def buscar_venda_por_id(id_venda):
    v = Venda()
    v.set_id(id_venda)
    return v.recuperar_dados()
