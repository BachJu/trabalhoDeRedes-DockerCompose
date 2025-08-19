from classes.bd.conexao import Conexao

'''
    idProduto INTEGER PRIMARY KEY,
    nome VARCHAR,
    preco INTEGER,
    quantidade INTEGER
'''

class Produto():
    __id: int
    __nome: str
    __preco: float
    __quantidade: int

    '''
    sets e gets
    '''
    def set_id(self, id_novo : int):
        self.__id = id_novo
    
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome : str):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_preco(self, preco : float):
        self.__preco = preco
    
    def get_preco(self):
        return self.__preco
    
    def set_quantidade(self, quantidade : int):
        self.__quantidade = quantidade
    
    def get_quantidade(self):
        return self.__quantidade
    
    '''
    Funções para realizar com o BD
    '''
    def inserir_produto(self):
        with Conexao() as con:
            nome = str(self.get_nome())
            preco = str(self.get_preco())
            quantidade = str(self.get_quantidade())

            sql_insert = "INSERT INTO Produto(nome, preco, quantidade)" \
            "                         VALUES (%s, %s, %s);"

            with con.cursor() as cursor:
                cursor.execute(sql_insert, (nome, preco, quantidade))
                con.commit()

    def deletar_produto(self):
        with Conexao() as con:
            id = str(self.get_id())

            sql_delete = "DELETE FROM Produto WHERE idProduto = %s;"

            with con.cursor() as cursor:
                cursor.execute(sql_delete, (id,))
                con.commit()

    def atualizar_produto(self):
        with Conexao() as con:
            id = str(self.get_id())
            nome = str(self.get_nome())
            preco = str(self.get_preco())
            quantidade = str(self.get_quantidade())

            sql_update = "UPDATE Produto" \
            "             SET nome = %s," \
            "                 preco = %s," \
            "                 quantidade = %s" \
            "             WHERE idProduto = %s;"

            with con.cursor() as cursor:
                cursor.execute(sql_update, (nome, preco, quantidade, id))
                con.commit()

    def recuperar_produtos(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Produto ORDER BY idProduto;"

            print("#"*50)
            print("Produtos:")
            print("-"*50)

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                print('\tidProduto | nome | Preco | quantidade')

                for record in cursor.fetchall():
                    print('-'*50)
                    print('\t', record[0], '|', record[1], '|', record[2], '|', record[3])

    def recuperar_ids(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Produto ORDER BY idProduto;"
            lista_id = []

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                for record in cursor.fetchall():
                    lista_id.append(int(record[0]))
                
                return lista_id

    def recuperar_dados(self):
        with Conexao() as con:
            id_recuperar = str(self.get_id())
            sql_select = "SELECT * FROM Produto WHERE idProduto = %s;"

            with con.cursor() as cursor:
                cursor.execute(sql_select, (id_recuperar,))
                lista = cursor.fetchall()

                return lista