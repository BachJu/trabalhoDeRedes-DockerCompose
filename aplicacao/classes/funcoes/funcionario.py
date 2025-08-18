from aplicacao.classes.telas import Tela
from aplicacao.classes.bd.funcionario import Funcionario

class funcao_Funcionario():

    def cadastrar_funcionario(self):
        Tela.limpaTela()
        Tela.separador()

        funcionario = Funcionario()

        nome = input("Digite o nome do funcionario: ")
        funcionario.set_nome(nome)
