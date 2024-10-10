--CREATE DATABASE redeFlex;

--USE redeFlex;

CREATE TABLE Cliente(
    ClienteId INT NOT NULL,
    NomeCliente VARCHAR(70) NOT NULL,
    Ativo VARCHAR(2) NOT NULL,
    PRIMARY KEY (ClienteId)
);

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

INSERT INTO Cliente (ClienteId, NomeCliente, Ativo) VALUES
(1, 'João Silva', 'S'),
(2, 'Osvaldo Dias', 'S'),
(3, 'Queren Hapuque', 'S'),
(4, 'Jemerson Franca', 'S'),
(5, 'Beatriz Amorim', 'S'),
(6, 'Gabriel Antonio', 'S'),
(7, 'Lucas Santos', 'S'),
(8, 'Juliana Alves', 'S'),
(9, 'Mariana Costa', 'S'),
(10, 'Pedro Martins', 'S');


INSERT INTO Produto (ProdutoId, NomeProduto) VALUES
(1, 'Produto A'),
(2, 'Carro'),
(3, 'Produto C'),
(4, 'Produto D'),
(5, 'Produto E'),
(6, 'Produto F'),
(7, 'Produto G'),
(8, 'Produto H'),
(9, 'Produto I'),
(10, 'Produto J');


INSERT INTO Venda (VendaId, ProdutoId, ClienteId, Valor, DataVenda) VALUES
(1, 1, 1, 100.00, '2024-10-01'),
(2, 2, 2, 35000.00, '2024-10-02'),
(3, 3, 3, 200.00, '2024-10-03'),
(4, 4, 4, 250.00, '2024-10-04'),
(5, 5, 5, 300.00, '2024-10-05'),
(6, 6, 6, 350.00, '2024-10-06'),
(7, 7, 7, 400.00, '2024-10-07'),
(8, 8, 8, 450.00, '2024-10-08'),
(9, 9, 9, 500.00, '2024-10-09'),
(10, 10, 10, 550.00, '2024-10-10');

SELECT * from Cliente;
SELECT* FROM Venda;
SELECT* from Produto;
--Selecionando as vendas 5 maiores vendas
SELECT*
FROM Venda
ORDER BY valor DESC
LIMIT 5;

SELECT C.ClienteId, C.NomeCliente, COUNT(V.VendaId) AS QuantidadeVendas, SUM(V.Valor) AS SomatorioValorVendas
FROM Cliente C
LEFT JOIN Venda V ON C.ClienteId = V.ClienteId
GROUP BY C.ClienteId, C.NomeCliente;

DELETE FROM Venda
WHERE ProdutoId IN (
    SELECT ProdutoId
    FROM Produto
    WHERE NomeProduto = 'carro'
) AND Valor > 30000;

UPDATE Cliente
SET Ativo = 'N'
WHERE ClienteId NOT IN (
    SELECT DISTINCT ClienteId
    FROM Venda
    WHERE DataVenda >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
);