CREATE TABLE IF NOT EXISTS bookinfo (
    nome VARCHAR(250),
    categoria VARCHAR(50),
    estrela INT,
    preco NUMERIC(5,2),
    estoque VARCHAR(50),
    PRIMARY KEY (nome)
);