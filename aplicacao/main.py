from classes.telas import Tela
from classes.funcoes.funcionario import *
from classes.funcoes.produto import *
from classes.funcoes.venda import *

tela = Tela()

while True:
    opcao = tela.tela_inicial()

    # ---------------- FUNCIONÁRIOS ----------------
    if opcao == 1:
        op_f = tela.tela_funcionario()
        if op_f == 1:  # adicionar
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cep = input("CEP: ")
            criar_funcionario(nome, email, telefone, cep)
            print("-"*50)
            print("Novo funcionario adicionado com sucesso.")

        elif op_f == 2:  # remover
            id_func = int(input("ID do funcionário: "))
            deletar_funcionario(id_func)
            print("-"*50)
            print("Informacoes de um funcionario deletada com sucesso.")

        elif op_f == 3:  # atualizar
            id_func = int(input("ID do funcionário: "))
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cep = input("CEP: ")
            atualizar_funcionario(id_func, nome, email, telefone, cep)
            print("-"*50)
            print("Informacoes atualizadas com sucesso.")

        elif op_f == 4:  # listar
            funcionarios = listar_funcionarios()
            if funcionarios is not None:
                for f in funcionarios:
                    print(f)
            else:
                print("-"*50)
                print("Fim da lista de funcionarios.")

    # ---------------- PRODUTOS ----------------
    elif opcao == 3:
        op_p = tela.tela_produto()
        if op_p == 1:
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            criar_produto(nome, preco, quantidade)
            print("-"*50)
            print("Novo produto adicionado com sucesso.")
        elif op_p == 4:
            produtos = listar_produtos()
            if produtos is not None:
                for p in produtos:
                    print(p)
            else:
                print("-"*50)
                print("Fim da lista de produtos.")

    # ---------------- VENDAS ----------------
    elif opcao == 2:
        op_v = tela.tela_venda()
        if op_v == 1:
            data = input("Data (YYYY-MM-DD): ")
            status = input("Status: ")
            id_funcionario = int(input("ID Funcionário: "))
            criar_venda(data, status, id_funcionario)
            print("-"*50)
            print("Nova venda adicionada com sucesso.")
        elif op_v == 4:
            vendas = listar_vendas()
            if vendas is not None:
                for v in vendas:
                    print(v)
            else:
                print("-"*50)
                print("Fim da lista de cendas")

    # ---------------- SAIR ----------------
    elif opcao == 9:
        print("Saindo do sistema...")
        break
