#Importar os dados

USE mercado_br;

DESCRIBE dados_cambio;

#Vamos começar a explorar nossa base de dados ao mesmo tempo que aprendemos a fazer consultas

SELECT * FROM cadastro_empresas;

SELECT * FROM dados_fechamento;

SELECT * FROM descricao_tempo;

#consulta com ordenação 

SELECT * FROM cadastro_empresas
ORDER BY stockCodeCompany DESC;

SELECT * FROM descricao_tempo
ORDER BY datetime DESC;

#selecionando colunas específicas

SELECT stockCodeCompany, segmentCompany
FROM cadastro_empresas;

SELECT keytime, keyCompany, closeValueStock FROM dados_fechamento;

/*
Exercicio 122:

Selecione todos os dados da tabela dados_cambio.

Exercício 123:

Selecione as colunas de abreviação e nome da moeda na tabela cadastro_moedas.

Exercício 124:

Selecione a tabela dados_cambio ordenando a coluna valueCoin de maneira decrescente. 


*/


SELECT * FROM dados_cambio;

SELECT abbrevCoin, nameCoin FROM cadastro_moedas;

SELECT * FROM dados_cambio
ORDER BY valueCoin DESC;








