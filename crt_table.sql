CREATE DATABASE IF NOT EXISTS trabalho;
USE trabalho;
CREATE TABLE IF NOT EXISTS Funcionario(
    id int(25) AUTO_INCREMENT,
    nome VARCHAR(30),
    email VARCHAR(50),
    telefone INTEGER,
    cep VARCHAR(30),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Venda (
    idVenda int(25) AUTO_INCREMENT,
    data DATE DEFAULT CURDATE(),
    status BOOLEAN,
    fk_funcionario_id INTEGER,
    PRIMARY KEY(idVenda)
);

CREATE TABLE IF NOT EXISTS Produto (
    idProduto int(25) AUTO_INCREMENT,
    nome VARCHAR(30),
    preco FLOAT(10, 2),
    quantidade INTEGER,
    PRIMARY KEY(idProduto)
);

CREATE TABLE IF NOT EXISTS Tem (
    idTem int(25) AUTO_INCREMENT,
    fk_produto_idProduto INTEGER,
    fk_venda_idVenda INTEGER,
    quantidadeVendida INTEGER,
    precoNaVenda FLOAT(10, 2),
    Desconto NUMERIC(10, 2)
);
 
ALTER TABLE Venda ADD CONSTRAINT FK_Venda_2
    FOREIGN KEY (fk_funcionario_id)
    REFERENCES Funcionario (id)
    ON DELETE RESTRICT;
 
ALTER TABLE Tem ADD CONSTRAINT FK_Tem_1
    FOREIGN KEY (fk_produto_idProduto)
    REFERENCES Produto (idProduto)
    ON DELETE RESTRICT;
 
ALTER TABLE Tem ADD CONSTRAINT FK_Tem_2
    FOREIGN KEY (fk_venda_idVenda)
    REFERENCES Venda (idVenda)
    ON DELETE RESTRICT;