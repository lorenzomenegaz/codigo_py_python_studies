
#Estrutura da query

INSERT INTO nome_da_tabela (column1, column2, column3) VALUES (value1, value2, value3);

USE codigopy;

#pro nosso caso, podemos fazer assim

INSERT INTO stocks (symbol, name, sector, price, volume) VALUES ('AAPL', 'Apple Inc.', 'Tecnologia', 102.34, 123456);

#para inserir várias informações ao mesmo tempo, podemos fazer assim:

INSERT INTO stocks (symbol, name, sector, price, volume) VALUES ('AAPL', 'Apple Inc.', 'Tecnologia', 102.34, 123456), 
																('GOOG', 'Google LLC', 'Tecnologia', 1234.56, 9876), 
                                                                ('FB', 'Facebook Inc.', 'Tecnologia', 90.12, 654321);
                                                                
#isso dificilmente vai ser usado, só pra dados específicos mesmo. No dia a dia você irá jogar dados do Python direto pro MySQL com o Pandas. Veremos isso em breve. 

#também é possível inserir apenas partes das informações

INSERT INTO stocks (symbol, price) VALUES ('PETR4', 20.21);

#o formato de data do MySQL é "ano-mes-dia"! O inverso do normal. 

INSERT INTO transactions (id, date, type, symbol, shares, price, customer_id) VALUES (1, '2022-12-05', 'compra', 'AAPL', 10, 102.34, 123);

INSERT INTO transactions (id, date, type, symbol, shares, price, customer_id) VALUES (2, '2022-12-05', 'venda', 'AAPL', 10, 102.34, 123);

DESCRIBE transactions;

/*
Exercicio 117:

Popule com dois exemplos de dados a tabela prices criada no exercício 116. Preencha todas as colunas com dados.

*/


INSERT INTO prices (date, symbol, open, high, low, close) VALUES ('2022-12-05', 'WEGE3', 30.45, 33.30, 30.00, 30.55), 
																	('2022-12-05', 'PETR4', 20.30, 21.54, 20.15, 20.24);






