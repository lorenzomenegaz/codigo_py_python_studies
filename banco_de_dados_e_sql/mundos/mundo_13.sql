#Qual a importância de chaves estrangeiras?

SELECT * FROM cadastro_moedas;

DELETE FROM cadastro_moedas WHERE keyCoin = 1;

#como juntar os dados das tabelas de câmbio?

SELECT * FROM dados_cambio
JOIN cadastro_moedas;

SELECT dados_cambio.keyTime, cadastro_moedas.nameCoin, dados_cambio.valueCoin FROM dados_cambio
JOIN cadastro_moedas;

#podemos abreviar as tabelas

SELECT dc.keyTime, c.nameCoin, dc.valueCoin FROM dados_cambio as dc
JOIN cadastro_moedas as c;

SELECT * FROM cadastro_moedas;
SELECT * FROM dados_cambio;

#quando especificamos quais as chaves em cada tabela, o join vem sem repetições

SELECT dc.keyTime, c.nameCoin, dc.valueCoin FROM dados_cambio as dc
INNER JOIN cadastro_moedas as c on c.keyCoin = dc.keyCoin;

#podemos colocar a clausula WHERE depois do join para apenas juntar determinadas chaves

SELECT dc.keyTime, c.nameCoin, dc.valueCoin FROM dados_cambio as dc
INNER JOIN cadastro_moedas as c on c.keyCoin = dc.keyCoin
WHERE c.keyCoin = 2;

#agora vamos juntar tres tabelas

SELECT dt.datetime, c.nameCoin, dc.valueCoin 
FROM dados_cambio as dc
INNER JOIN cadastro_moedas as c on c.keyCoin = dc.keyCoin
INNER JOIN descricao_tempo as dt on dt.keyTime = dc.keyTime;

#puxando dados de moedas em determinados períodos

SELECT dt.datetime, c.nameCoin, dc.valueCoin 
FROM dados_cambio as dc
INNER JOIN cadastro_moedas as c on c.keyCoin = dc.keyCoin
INNER JOIN descricao_tempo as dt on dt.keyTime = dc.keyTime
WHERE c.nameCoin = "DOLAR" AND dt.datetime BETWEEN 2010 AND 2014;

SELECT * FROM dados_cambio;

INSERT INTO dados_cambio VALUES (4, 3, 1);
												
SELECT dt.datetime, c.nameCoin, dc.valueCoin FROM dados_cambio as dc
LEFT JOIN cadastro_moedas as c on c.keyCoin = dc.keyCoin
INNER JOIN descricao_tempo as dt on dt.keyTime = dc.keyTime;

#Outros tipos de Join

USE codigopy;

SELECT * FROM customers;
SELECT * FROM movimentacoes;

INSERT INTO customers VALUES (1, "Brenno", "brennola@outlook.com", "97856-9081"),
							(2, "Leandro", "leandrola@outlook.com", "97856-9081");

INSERT INTO movimentacoes VALUES (10, "2020-01-01", "compra", "WEGE3", 100, 20.34, 1),
							(11, "2020-01-01", "compra", "PETR4", 100, 23.54, 2),
                            (12, "2020-01-01", "compra", "LREN3", 100, 34.90, 3);

SELECT u.name, m.date, m.type, m.symbol FROM movimentacoes as m
LEFT JOIN customers as u on m.customer_id = u.customer_id;

USE mercado_br;

SELECT * FROM cadastro_empresas;
SELECT * FROM dados_fechamento;

SELECT c.stockCodeCompany, c.nameCompany, df.closeValueStock FROM dados_fechamento as df
INNER JOIN cadastro_empresas as c on c.keyCompany = df.keyCompany;

/*
Exercício 130:

Selecione a coluna nome, código e fechamento das tabelas cadastro_empresas e dados_fechamento, utilizando chaves e um INNER JOIN.

Exercício 131:

Selecione a coluna nome, código, datetime e fechamento das tabelas cadastro_empresas, dados_fechamento e descricao_tempo. Ordene da data mais antiga para a mais nova.

Exercício 132:

Selecione as cotações da WEGE3 entre 2018 e 2022.

*/


SELECT c.stockCodeCompany, c.nameCompany, df.closeValueStock FROM dados_fechamento as df
INNER JOIN cadastro_empresas as c on c.keyCompany = df.keyCompany;


SELECT dt.datetime, c.stockCodeCompany, c.nameCompany, df.closeValueStock FROM dados_fechamento as df
INNER JOIN cadastro_empresas as c on c.keyCompany = df.keyCompany
INNER JOIN descricao_tempo as dt on dt.keyTime = df.keyTime
ORDER BY dt.datetime;

SELECT dt.datetime, c.stockCodeCompany, c.nameCompany, df.closeValueStock FROM dados_fechamento as df
INNER JOIN cadastro_empresas as c on c.keyCompany = df.keyCompany
INNER JOIN descricao_tempo as dt on dt.keyTime = df.keyTime
WHERE c.stockCodeCompany = "WEGE3" AND dt.datetime BETWEEN 2018 AND 2022;

