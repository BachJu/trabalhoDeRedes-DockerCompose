from os import system, name
from classes.funcionario import Funcionario
from classes.produto import Produto
from classes.venda import Venda

class Tela():

    def limpaTela(self):
        '''
        Limpa a tela de acordo com o sistema operacional
        '''
        if name == 'nt':
            _ = system("cls")
        else:
            _ = system("clear")
    
    def separador(self):
        '''
        Imprime um separador para melhor visualização no terminal
        '''
        print("#"*50)

    def tela_inicial(self):
        '''
        Tela inicial
        
        Retorno
        -------
        Retorna a opção escolhida pelo usuário    
        '''
        self.limpaTela()
        self.separador()
        print("SISTEMA DE UM MERCADO :) \n")
        self.separador()

        opcoes = [1, 2, 3, 9]
        opcao = 10

        while opcao not in opcoes:
            self.separador()
            print("[1] Funcionario\n" \
            "      [2] Venda\n" \
            "      [3] Produto\n" \
            "      [9] Sair do programa\n")
            print("-"*50)
            opcao = int(input("Opcao: "))
            self.separador()
        
        return opcao
    
    def tela_funcionario(self):
        '''
        Tela de menu das opções de funcionarios
        '''
        self.limpaTela()
        self.separador()
        print("MENU - FUNCIONARIOS\n")
        self.separador()

        opcoes = [1, 2, 3, 4, 9]
        opcao = 10

        while opcoes not in opcoes:
            self.separador()
            print("[1] Adicionar novo funcionario\n" \
            "      [2] Remover um funcionario\n" \
            "      [3] Atualizar informacoes de um funcionario\n" \
            "      [4] Listar todos os funcionario\n" \
            "      [9] Sair")