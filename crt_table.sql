/* Lógico_1: */

CREATE TABLE Funcionario (
    Id INTEGER PRIMARY KEY,
    Nome VARCHAR,
    Email VARCHAR,
    Telefone INTEGER,
    CEP VARCHAR
);

CREATE TABLE Venda (
    IdVenda INTEGER PRIMARY KEY,
    Data NUMERIC,
    Status VARCHAR,
    fk_Funcionario_Id INTEGER
);

CREATE TABLE Produto (
    IdProduto INTEGER PRIMARY KEY,
    Nome VARCHAR,
    preco INTEGER,
    Quantidade INTEGER
);

CREATE TABLE Tem (
    fk_Produto_IdProduto INTEGER,
    fk_Venda_IdVenda INTEGER,
    QuantidadeVendida INTEGER,
    PrecoNaVenda INTEGER,
    Desconto INTEGER
);
 
ALTER TABLE Venda ADD CONSTRAINT FK_Venda_2
    FOREIGN KEY (fk_Funcionario_Id)
    REFERENCES Funcionario (Id)
    ON DELETE RESTRICT;
 
ALTER TABLE Tem ADD CONSTRAINT FK_Tem_1
    FOREIGN KEY (fk_Produto_IdProduto)
    REFERENCES Produto (IdProduto)
    ON DELETE RESTRICT;
 
ALTER TABLE Tem ADD CONSTRAINT FK_Tem_2
    FOREIGN KEY (fk_Venda_IdVenda)
    REFERENCES Venda (IdVenda)
    ON DELETE RESTRICT;