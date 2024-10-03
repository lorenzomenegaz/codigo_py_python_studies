#Como manipular linhas?

UPDATE nome_tabela
SET coluna = valor_novo
WHERE condicao_de_troca;

SELECT * FROM acoes; 

UPDATE acoes
SET sector = "Tech"
WHERE id = 1;

UPDATE acoes
SET sector = "Tech"
WHERE sector = "Tecnologia";

#para usar uma condição que não é uma chave primária, teremos que fazer um comando a mais.

UPDATE acoes
SET sector = "Petroleira"
WHERE simbolo = "PETR4"; 

SET SQL_SAFE_UPDATES = 0; #isso é uma protação contra você alterar muitas linhas de uma só vez.

#mudar diferentes colunas de uma só vez

UPDATE acoes
SET volume = 10000, name = "Petrobras"
WHERE id = 5;

#deletar uma linha

DELETE FROM acoes
where simbolo = 'AAPL';

SELECT * FROM acoes; 

INSERT INTO acoes (simbolo, name, sector, price, volume) VALUES ('AAPL', 'Apple Inc.', 'Tecnologia', 102.34, 123456);

#CUIDADO! NO MySQL não tem ctrl z. Você precisa se proteger através de backups (veremos na próxima aula)

/*
Exercicio 120:

Na tabela acoes, mude o símbolo FB para META e o nome da empresa Facebook Inc para Meta Inc.

Exercicio 121:

Na tabela acoes, delete as informações do Google.


*/


UPDATE acoes
SET simbolo = "META", name = "Meta Inc"
WHERE simbolo = "FB";

DELETE FROM acoes
where simbolo = "GOOG";

SELECT * FROM acoes;












































