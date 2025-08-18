from aplicacao.classes.bd.conexao import Conexao

'''
    fk_Produto_IdProduto INTEGER,
    fk_Venda_IdVenda INTEGER,
    QuantidadeVendida INTEGER,
    PrecoNaVenda NUMERIC(10, 2),
    Desconto NUMERIC(10, 2)
'''

class Tem():
    __idProduto: int
    __idVenda: int
    __qtdVendida: int
    __precoNaVenda: float
    __desconto: float

    '''
    sets e gets
    '''
    def set_idProduto(self, id_produto : int):
        self.__idProduto = id_produto
    
    def get_idProduto(self):
        return self.__idProduto
    
    def set_idVenda(self, id_venda : int):
        self.__idVenda = id_venda
    
    def get_idVenda(self):
        return self.__idVenda
    
    def set_qtdVendidas(self, qtdVendidas : int):
        self.__qtdVendida = qtdVendidas
    
    def get_qtdVendidas(self):
        return self.__qtdVendida
    
    def set_precoNasVendas(self, precoNaVenda : float):
        self.__precoNaVenda = precoNaVenda

    def get_precoNasVendas(self):
        return self.__precoNaVenda
    
    def set_desconto(self, desconto : float):
        self.__desconto = desconto

    def get_desconto(self):
        return self.__desconto
