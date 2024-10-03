USE codigopy;

DESCRIBE stocks;

SELECT * FROM stocks;

#colocando uma coluna nova

ALTER TABLE stocks
ADD COLUMN price_date DATE after symbol;

#excluindo coluna nova

ALTER TABLE stocks
DROP COLUMN price_date;

#mudando o tipo da coluna

ALTER TABLE stocks
MODIFY COLUMN symbol VARCHAR(20) NOT NULL;

#mudando o nome da coluna

ALTER TABLE stocks
CHANGE COLUMN symbol simbolo VARCHAR(20) NOT NULL;

#Mudando o nome da tabela inteira

ALTER TABLE stocks
RENAME TO acoes;

ALTER TABLE prices
CHANGE COLUMN close fechamento DECIMAL(10,3) NOT NULL;

ALTER TABLE prices
RENAME TO movimentacoes;


/*
Exercicio 118:

Altere a tabela prices e exija que a coluna close não seja nula, permita 3 casas decimais e tenha um novo nome chamado "fechamento".

Exercício 119:

Altere o nome da tabela "transactions" para "movimentacoes" 

*/


ALTER TABLE prices
CHANGE COLUMN close fechamento DECIMAL(10, 3) NOT NULL;

DESCRIBE prices;

ALTER TABLE transactions
RENAME TO movimentacoes;
