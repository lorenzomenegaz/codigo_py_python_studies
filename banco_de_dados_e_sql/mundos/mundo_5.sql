#os comandos SQL são separados por ";" e para rodar basta clicar "ctrl" e "enter".

CREATE DATABASE codigopy;

DROP DATABASE codigopy;

USE codigopy;


#acostumem criar nomes em ingles. Não é possível criar nomes acentuados.

CREATE TABLE stocks (
  id INT PRIMARY KEY AUTO_INCREMENT, #não existem mais de 2 bilhões de ações
  symbol VARCHAR(10) NOT NULL, #isso aqui também poderia ser a chave primária #WEGE3 PETR4
  name VARCHAR(100),
  sector VARCHAR(50) DEFAULT 'Indefinido',
  price DECIMAL(10,2), #quantos números totais e quantas casas decimais. Detalhe: não é possível ter mais decimais que números totais, obviamente.
  volume BIGINT
);

DESCRIBE stocks;

DROP TABLE stocks;


#podemos criar a tabela de transações também

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  date DATE,
  type ENUM('compra', 'venda'), #o tipo ENUM determina uma lista de valores que podem ser colocados nessa coluna. Aqui os tipos pré definidos são de compra ou venda. 
  symbol VARCHAR(10),
  shares INTEGER UNSIGNED,
  price DECIMAL(10,2),
  customer_id INTEGER #isso aqui é uma chave estrangeira
);

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(255),
  phone VARCHAR(15)
);

DROP TABLE customers;

CREATE TABLE prices (
  id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  symbol VARCHAR(10) NOT NULL,
  open DECIMAL(10,2),
  high DECIMAL(10,2),
  low DECIMAL(10,2),
  close DECIMAL(10,2)
);

/*
Exercicio 116:

Crie uma tabela chamada prices que armazene informações sobre preços. A tabela deve ter as seguintes colunas:

id: um identificador único para cada preço 
date: a data do preço 
symbol: o símbolo que representa aquele preço 
open: abertura do dia 
high: máxima do dia 
low: mínima do dia 
close: fechamento do dia 

Configure os tipos de dados corretamente e atribua a característica "not null" a colunas fundamentais. 

*/


CREATE TABLE prices (
  id INTEGER PRIMARY KEY auto_increment,
  date DATE NOT NULL,
  symbol VARCHAR(10) NOT NULL,
  open DECIMAL(10,2),
  high DECIMAL(10,2),
  low DECIMAL(10,2),
  close DECIMAL(10,2) 
);



















