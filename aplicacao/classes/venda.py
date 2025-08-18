from classes.conexao import Conexao

'''
    IdVenda INTEGER PRIMARY KEY,
    Data NUMERIC,
    Status VARCHAR,
    fk_Funcionario_Id INTEGER
'''

class Venda():
    __id: int
    __data: float
    __status: str
    __fkFuncionarioId: int

    '''
    sets e gets
    '''
    def set_id(self, id_novo : int):
        self.__id = id_novo
    
    def get_id(self):
        return self.__id
    
    def set_data(self, data : float):
        self.__data = data

    def get_data(self):
        return self.__data
    
    def set_status(self, status : str):
        self.__status = status

    def get_status(self):
        return self.__status
    
    def set_fkFuncionarioId(self, fkFuncionarioId : int):
        self.__fkFuncionarioId = fkFuncionarioId
    
    def get_fkFuncionarioId(self):
        return self.__fkFuncionarioId
    
    '''
    Funções para realizar com o BD
    '''

    