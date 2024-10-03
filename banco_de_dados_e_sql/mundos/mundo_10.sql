CREATE DATABASE mercado_br;

#https://www.kaggle.com/datasets/leomauro/brazilian-stock-market-data-warehouse?select=factCoins.csv
#https://datasetsearch.research.google.com/

#quando separar ou não os dados? Como modelar?
#A informação pode mudar a ponto de te afundar? 
#A informação é uma classificação com várias caraterísticas? 
#Passou de 10 colunas se pergunte se você não deveria criar uma chave primária pra alguma informação que se repete muito. 

USE mercado_br;
 
DROP TABLE IF EXISTS `factStocks`;
DROP TABLE IF EXISTS `factCoins`;
DROP TABLE IF EXISTS `dimTime`;
DROP TABLE IF EXISTS `dimCoin`; 
DROP TABLE IF EXISTS `dimCompany`;

CREATE TABLE `cadastro_empresas` (
	`keyCompany` INT NOT NULL,
	`stockCodeCompany` VARCHAR(32) NOT NULL,
	`nameCompany` VARCHAR(64) NOT NULL,
	`sectorCodeCompany` VARCHAR(32) NOT NULL,
	`sectorCompany` VARCHAR(256) NOT NULL,
	`segmentCompany` VARCHAR(256) NOT NULL,
	CONSTRAINT companyPK PRIMARY KEY (keyCompany)
);

CREATE TABLE `cadastro_moedas` (
	`keyCoin` INT NOT NULL,
	`abbrevCoin` VARCHAR(32) NOT NULL,
	`nameCoin` VARCHAR(32) NOT NULL,
	`symbolCoin` VARCHAR(8) NOT NULL,
	CONSTRAINT coinPK PRIMARY KEY (keyCoin)
);

CREATE TABLE `descricao_tempo` (
	`keyTime` INT NOT NULL,
	`datetime` VARCHAR(32) NOT NULL,
	`dayTime` SMALLINT NOT NULL,
	`dayWeekTime` SMALLINT NOT NULL,
	`dayWeekAbbrevTime` VARCHAR(32) NOT NULL,
	`dayWeekCompleteTime` VARCHAR(32) NOT NULL,
	`monthTime` SMALLINT NOT NULL,
	`monthAbbrevTime` VARCHAR(32) NOT NULL,
	`monthCompleteTime` VARCHAR(32) NOT NULL,
	`bimonthTime` SMALLINT NOT NULL,
	`quarterTime` SMALLINT NOT NULL,
	`semesterTime` SMALLINT NOT NULL,
	`yearTime` INT NOT NULL,
	CONSTRAINT timePK PRIMARY KEY (keyTime)
);

CREATE TABLE `dados_cambio` (
	`keyTime` INT NOT NULL,
	`keyCoin` INT NOT NULL,
	`valueCoin` FLOAT NOT NULL,
    FOREIGN KEY (keyTime) REFERENCES descricao_tempo(keyTime),
    FOREIGN KEY (keyCoin) REFERENCES cadastro_moedas(keyCoin),
    CONSTRAINT coinsPK PRIMARY KEY(keyTime, keyCoin)
);

CREATE TABLE `dados_fechamento` (
	`keyTime` INT NOT NULL,
	`keyCompany` INT NOT NULL,
	`openValueStock` FLOAT NOT NULL,
	`closeValueStock` FLOAT NOT NULL,
	`highValueStock` FLOAT NOT NULL,
	`lowValueStock` FLOAT NOT NULL,
	`quantityStock` FLOAT NOT NULL,
    FOREIGN KEY (keyTime) REFERENCES descricao_tempo(keyTime),
    FOREIGN KEY (keyCompany) REFERENCES cadastro_empresas(keyCompany),
    CONSTRAINT stocksPK PRIMARY KEY(keyTime, keyCompany) #essa constraint é uma condição, ou seja, essas duas colunas devem ser únicas em conjunto.
    #caso dê erro de duplicata, o mysql irá retornar que a constraint stocksPK foi violada. 
);


