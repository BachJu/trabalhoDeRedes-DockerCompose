from aplicacao.classes.bd.funcionario import Funcionario

def criar_funcionario(nome, email, telefone, cep):
    f = Funcionario()
    f.set_nome(nome)
    f.set_email(email)
    f.set_telefone(telefone)
    f.set_cep(cep)
    f.inserir_funcionario()

def listar_funcionarios():
    f = Funcionario()
    return f.recuperar_funcionarios()

def atualizar_funcionario(id_funcionario, nome, email, telefone, cep):
    f = Funcionario()
    f.set_id(id_funcionario)
    f.set_nome(nome)
    f.set_email(email)
    f.set_telefone(telefone)
    f.set_cep(cep)
    f.atualizar_funcionario()

def deletar_funcionario(id_funcionario):
    f = Funcionario()
    f.set_id(id_funcionario)
    f.deletar_funcionario()

def buscar_funcionario_por_id(id_funcionario):
    f = Funcionario()
    f.set_id(id_funcionario)
    return f.recuperar_dados()