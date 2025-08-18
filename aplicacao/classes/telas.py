import os
from classes.funcoes.funcionario import (
    criar_funcionario, listar_funcionarios, atualizar_funcionario,
    deletar_funcionario, buscar_funcionario_por_id
)
from classes.funcoes.produto import (
    criar_produto, listar_produtos, atualizar_produto,
    deletar_produto, buscar_produto_por_id
)
from classes.funcoes.venda import (
    criar_venda, listar_vendas, atualizar_venda,
    deletar_venda, buscar_venda_por_id
)


class Tela():

    def limpaTela(self):
        '''
        Limpa a tela de acordo com o sistema operacional
        '''
        if os.name == 'nt':
            _ = os.system("cls")
        else:
            _ = os.system("clear")
    
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

        Retorno
        -------
        Retorna a opção escolhida pelo usuário 
        '''
        self.limpaTela()
        self.separador()
        print("MENU - FUNCIONARIOS\n")
        self.separador()

        opcoes = [1, 2, 3, 4, 9]
        opcao = 10

        while opcao not in opcoes:
            self.separador()
            print("[1] Adicionar novo funcionario\n" \
            "      [2] Remover um funcionario\n" \
            "      [3] Atualizar informacoes de um funcionario\n" \
            "      [4] Listar todos os funcionario\n" \
            "      [9] Sair")
            print("-"*50)
            opcao = int(input("Opcao: "))
            self.separador()
        
        return opcao
    
    def tela_venda(self):
        '''
        Tela de menu das opções de venda

        Retorno
        -------
        Retorna a opção escolhida pelo usuário 
        '''
        self.limpaTela()
        self.separador()
        print("MENU - VENDA\n")
        self.separador()

        opcoes = [1, 2, 3, 4, 9]
        opcao = 10

        while opcao not in opcoes:
            self.separador()
            print("[1] Adicionar nova venda\n" \
            "      [2] Remover uma venda\n" \
            "      [3] Atualizar informacoes de uma venda\n" \
            "      [4] Listar todos as vendas\n" \
            "      [9] Sair")
            print("-"*50)
            opcao = int(input("Opcao: "))
            self.separador()
        
        return opcao
    
    def tela_produto(self):
        '''
        Tela de menu das opções de produto

        Retorno
        -------
        Retorna a opção escolhida pelo usuário
        '''
        self.limpaTela()
        self.separador()
        print("MENU - PRODUTO\n")
        self.separador()

        opcoes = [1, 2, 3, 4, 9]
        opcao = 10

        while opcao not in opcoes:
            self.separador()
            print("[1] Adicionar novo produto\n" \
            "      [2] Remover um produto\n" \
            "      [3] Atualizar informacoes de um produto\n" \
            "      [4] Listar todos os produto\n" \
            "      [9] Sair")
            print("-"*50)
            opcao = int(input("Opcao: "))
            self.separador()
        
        return opcao