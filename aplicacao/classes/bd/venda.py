from classes.bd.conexao import Conexao

'''
    idVenda INTEGER PRIMARY KEY,
    data NUMERIC,
    status VARCHAR,
    fk_funcionario_id INTEGER
'''

class Venda():
    __id: int
    __data: float
    __status: str
    __IdFuncionario: int

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
    
    def set_IdFuncionario(self, IdFuncionario : int):
        self.__IdFuncionario = IdFuncionario
    
    def get_IdFuncionario(self):
        return self.__IdFuncionario
    
    '''
    Funções para realizar com o BD
    '''
    def inserir_venda(self):
        with Conexao() as con:
            data = str(self.get_data())
            status = str(self.get_status())
            IdFuncionario = str(self.get_IdFuncionario())

            sql_insert = "INSERT INTO Venda(data, status, fk_funcionario_id)" \
            "                         VALUES (%s, %s, %s);"

            with con.cursor() as cursor:
                cursor.execute(sql_insert, (data, status, IdFuncionario))
                con.commit()

    def deletar_venda(self):
        with Conexao() as con:
            id = str(self.get_id())

            sql_delete = "DELETE FROM Venda WHERE idVenda = %s;" 

            with con.cursor() as cursor:
                cursor.execute(sql_delete, (id,))
                con.commit()

    def atualizar_venda(self):
        with Conexao() as con:
            id = str(self.get_id())
            data = str(self.get_data())
            status = str(self.get_status())
            IdFuncionario = str(self.get_IdFuncionario())

            sql_update = "UPDATE Venda" \
            "             SET data = %s," \
            "                 status = %s," \
            "                 fk_funcionario_id = %s" \
            "             WHERE idVenda = %s;"

            with con.cursor() as cursor:
                cursor.execute(sql_update, (data, status, IdFuncionario, id))
                con.commit()

    def recuperar_vendas(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Venda ORDER BY idVenda;"

            print("#"*50)
            print("Vendas:\n")
            print("-"*50)

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                print('\tidVenda | data | status | IdFuncionario')

                for record in cursor.fetchall():
                    print('\t', record[0], '|', record[1], '|', record[2], '|', record[3])

            print("#"*50)

    def recuperar_ids(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Venda ORDER BY idVenda;"
            lista_id = []

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                for record in cursor.fetchall():
                    lista_id.append(int(record[0]))
                
                return lista_id

    def recuperar_dados(self):
        with Conexao() as con:
            id_recuperar = str(self.get_id())
            sql_select = "SELECT * FROM Venda WHERE idVenda = %s;"

            with con.cursor() as cursor:
                cursor.execute(sql_select, (id_recuperar,))
                lista = cursor.fetchall()

                return lista