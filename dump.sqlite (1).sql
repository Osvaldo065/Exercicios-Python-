-- TABLE
CREATE TABLE Cliente(
    ClienteId INT NOT NULL,
    NomeCliente VARCHAR(70) NOT NULL,
    Ativo VARCHAR(2) NOT NULL,
    PRIMARY KEY (ClienteId)
);
CREATE TABLE demo (ID integer primary key, Name varchar(20), Hint text );
CREATE TABLE Produto(
    ProdutoId INT NOT NULL,
    NomeProduto VARCHAR(90) NOT NULL,
    PRIMARY KEY (ProdutoId)
);
CREATE TABLE Venda(
    VendaId INT NOT NULL,
    ProdutoId INT NOT NULL,
    ClienteId INT NOT NULL,
    Valor DECIMAL NOT NULL,
    DataVenda DATE NOT NULL,
    PRIMARY KEY (VendaId),
    FOREIGN KEY (ProdutoId) REFERENCES Produto(ProdutoId),
    FOREIGN KEY (ClienteId) REFERENCES Cliente(ClienteId)
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
