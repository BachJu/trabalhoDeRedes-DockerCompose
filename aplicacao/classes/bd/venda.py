from classes.bd.conexao import Conexao

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
        return self.__fkFuncionarioId
    
    '''
    Funções para realizar com o BD
    '''
    def inserir_venda(self):
        with Conexao() as con:
            data = str(self.get_data())
            status = str(self.get_status())
            IdFuncionario = str(self.get_IdFuncionario())

            sql_insert = "INSERT INTO Venda(Data, Status, fk_Funcionario_Id)" \
            "                         VALUES ({%s}, {%s}, {%s}, {%s});" % (data, status, IdFuncionario)

            with con.cursor() as cursor:
                cursor.execute(sql_insert)
                con.commit()

    def deletar_venda(self):
        with Conexao() as con:
            id = str(self.get_id())

            sql_delete = "DELETE FROM Venda WHERE IdVenda = {%s};" % id 

            with con.cursor() as cursor:
                cursor.execute(sql_delete)
                con.commit()

    def atualizar_venda(self):
        with Conexao() as con:
            id = str(self.get_id())
            data = str(self.get_data())
            status = str(self.get_status())
            IdFuncionario = str(self.get_IdFuncionario())

            sql_update = "UPDATE Venda" \
            "             SET Data = {%s}," \
            "                 Status = {%s}," \
            "                 fk_Funcionario_Id = {%s}," \
            "             WHERE IdVenda = {%s};" % (data, status, IdFuncionario, id)

            with con.cursor() as cursor:
                cursor.execute(sql_update)
                con.commit()

    def recuperar_vendas(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Venda ORDER BY IdVenda;"

            print("#"*50)
            print("Vendas:\n")
            print("-"*50)

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                print('\tIdVenda | data | status | IdFuncionario')

                for record in cursor.fetchall():
                    print('-'*50)
                    print("\t")
                    print(record[0], '|', record[1], '|', record[2], '|', record[3])

            print("#"*50)

    def recuperar_ids(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Venda ORDER BY IdVenda;"
            lista_id = []

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                for record in cursor.fetchall():
                    lista_id.append(int(record[0]))
                
                return lista_id

    def recuperar_dados(self):
        with Conexao() as con:
            id_recuperar = str(self.get_id())
            sql_select = "SELECT * FROM Venda WHERE IdVenda = {%s};" % id_recuperar

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                lista = cursor.fetchall()

                return lista