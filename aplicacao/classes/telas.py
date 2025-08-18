from os import system, name
from classes.funcionario import Funcionario

class Tela():

    def limpaTela():
        '''
        Limpa a tela de acordo com o sistema operacional
        '''
        if name == 'nt':
            _ = system("cls")
        else:
            _ = system("clear")

    