from classes.bd.conexao import Conexao

'''
    Id INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Email VARCHAR,
    Telefone INTEGER,
    CEP VARCHAR
'''

class Funcionario():
    __id: int
    __nome: str
    __email: str
    __telefone: int
    __cep: str

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
    
    def set_email(self, email : str):
        self.__email = email
    
    def get_email(self):
        return self.__email

    def set_telefone(self, telefone : int):
        self.__telefone = telefone
    
    def get_telefone(self):
        return self.__telefone

    def set_cep(self, cep : str):
        self.__cep = cep

    def get_cep(self):
        return self.__cep

    '''
    Funções para realizar com o BD
    '''
    def inserir_funcionario(self):
        with Conexao() as con:
            nome = str(self.get_nome())
            email = str(self.get_email())
            telefone = str(self.get_telefone())
            cep = str(self.get_cep())

            sql_insert = "INSERT INTO Funcionario(Nome, Email, Telefone, CEP)" \
            "                         VALUES ({}, {}, {}, {});".format(nome, email, telefone, cep)

            with con.cursor() as cursor:
                cursor.execute(sql_insert)
                con.commit()

    def deletar_funcionario(self):
        with Conexao() as con:
            id = str(self.get_id())

            sql_delete = "DELETE FROM Funcionario WHERE Id = {};".format(id) 

            with con.cursor() as cursor:
                cursor.execute(sql_delete)
                con.commit()

    def atualizar_funcionario(self):
        with Conexao() as con:
            id = str(self.get_id())
            nome = str(self.get_nome())
            email = str(self.get_email())
            telefone = str(self.get_telefone())
            cep = str(self.get_cep())

            sql_update = "UPDATE Funcionario" \
            "             SET Nome = {}," \
            "                 Email = {}," \
            "                 Telefone = {}," \
            "                 CEP = {}" \
            "             WHERE Id = {};".format(nome, email, telefone, cep, id)

            with con.cursor() as cursor:
                cursor.execute(sql_update)
                con.commit()

    def recuperar_funcionarios(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Funcionario ORDER BY Id;"

            print("#"*50)
            print("Funcionarios:\n")
            print("-"*50)

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                print('\tID | nome | email | telefone | CEP')

                for record in cursor.fetchall():
                    print('-'*50)
                    print("\t")
                    print(record[0], '|', record[1], '|', record[2], '|', record[3], '|', record[4])

            print("#"*50)

    def recuperar_ids(self):
        with Conexao() as con:
            sql_select = "SELECT * FROM Funcionario ORDER BY Id;"
            lista_id = []

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                for record in cursor.fetchall():
                    lista_id.append(int(record[0]))
                
                return lista_id

    def recuperar_dados(self):
        with Conexao() as con:
            id_recuperar = str(self.get_id())
            sql_select = "SELECT * FROM Funcionario WHERE Id = {};".format(id_recuperar)

            with con.cursor() as cursor:
                cursor.execute(sql_select)
                lista = cursor.fetchall()

                return lista