#Como selecionar linhas a partir de condições?

SELECT * FROM cadastro_moedas;

SELECT * FROM dados_cambio
ORDER BY valueCoin DESC;

SELECT * FROM dados_cambio
WHERE keyCoin = 1
ORDER BY valueCoin DESC;

SELECT * FROM dados_cambio
WHERE keyCoin = 1;


#Podemos fazer com tempo também

SELECT * FROM descricao_tempo;

SELECT * FROM descricao_tempo
WHERE yearTime = 2000;


#podemos usar condicionais igual no Python com as cláusulas AND e OR. Bem parecido com as condicionais do Python mesmo

SELECT * FROM descricao_tempo
WHERE yearTime = 2000 AND monthCompleteTime = "FEVEREIRO";

SELECT * FROM descricao_tempo
WHERE dayWeekAbbrevTime = "SEG" OR dayWeekCompleteTime = "SABADO";

SELECT * FROM descricao_tempo
WHERE (dayWeekAbbrevTime = "SEG" OR dayWeekCompleteTime = "SABADO") AND 
		(yearTime = 2000 OR yearTime = 2001); #por isso que depois da primeira linguagem que você aprende, o resto é infinitamente mais fácil.

#No python podemos fazer condionais utilizando "in" com uma lista. No SQL podemos fazer o mesmo.

SELECT * FROM descricao_tempo
WHERE dayWeekAbbrevTime IN ("SEG", "TER");

SELECT * FROM descricao_tempo
WHERE dayWeekAbbrevTime NOT IN ("SEG", "TER");

#Trabalhando datas, podemos usar o operador "between"

SELECT * FROM descricao_tempo
WHERE yearTime BETWEEN 2000 AND 2003; #vamos usar isso aqui quando juntarmos as tabelas e quisermos selecionar um periodo de cotações de uma determinada empresa

SELECT * FROM descricao_tempo
WHERE datetime BETWEEN 2014 AND 2016;

#também serve pra números ou ordem alfabética

SELECT * FROM dados_cambio
WHERE valueCoin BETWEEN 2 AND 4;

SELECT * FROM cadastro_empresas
WHERE nameCompany BETWEEN "BRADESPAR" AND "DEXXOS PAR"
ORDER BY nameCompany;

#Mas e se eu quiser puxar a lista de nome das empresas, sem duplicatas?

SELECT DISTINCT nameCompany FROM cadastro_empresas
WHERE nameCompany BETWEEN "BRADESPAR" AND "DEXXOS PAR"
ORDER BY nameCompany;

#Como pegar todas as empresas da base
SELECT DISTINCT nameCompany FROM cadastro_empresas;

#Pra finalizar, se eu quiser todas as empresas que tem S.A. no nome?

SELECT DISTINCT nameCompany FROM cadastro_empresas
WHERE nameCompany LIKE "%S.A.%"; #o % subistui nenhum ou vários caracteres. 

#Todas as empresas que começam com W

SELECT DISTINCT nameCompany FROM cadastro_empresas
WHERE nameCompany LIKE "W%";

SELECT DISTINCT nameCompany FROM cadastro_empresas
WHERE nameCompany LIKE "%A";


/*
Exercício 125:

Selecione as linhas na tabela cadastro_empresas onde o nome da empresa é "WEG"

Exercício 126:

Selecione empresas da tabela cadastro_empresas que estão presentes no SMLL ou IGNM (coluna sectorCodeCompany).

Exercício 127:

Selecione empresas da tabela cadastro_empresas que estão no SMLL e possuem final "3" no código.

Exercício 128:

Extraia a lista de todos os setores que existem na tabela cadastro_empresas (coluna sectorCompany)

Exercício 129:

Selecione as linhas entre o ano 2010 e 2014 da tabela descricao_tempo.

*/

SELECT * FROM cadastro_empresas
WHERE nameCompany = "WEG";

SELECT * FROM cadastro_empresas
WHERE sectorCodeCompany IN ("SMLL", "IGNM");

SELECT * FROM cadastro_empresas
WHERE sectorCodeCompany = "SMLL" OR sectorCodeCompany = "IGNM";

SELECT * FROM cadastro_empresas
WHERE sectorCodeCompany = "SMLL" AND stockCodeCompany LIKE "%3";

SELECT DISTINCT sectorCompany FROM cadastro_empresas;

SELECT * FROM descricao_tempo
WHERE datetime BETWEEN 2010 AND 2014;





