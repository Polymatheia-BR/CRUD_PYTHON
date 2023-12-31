DROP TABLE IF EXISTS alunos;
CREATE TABLE alunos (
  matricula int NOT NULL AUTO_INCREMENT,
  nome varchar(255) NOT NULL,
  CPF char(11) NOT NULL,
  telefone char(11) NOT NULL,
  endereco varchar(255) NOT NULL,
  PRIMARY KEY (`matricula`)
);

DROP TABLE IF EXISTS funcionario;
CREATE TABLE funcionario (
  id_funcionario int NOT NULL AUTO_INCREMENT,
  nome varchar(120) NOT NULL,
  CPF char(11) NOT NULL,
  departamento int NOT NULL,
  salario decimal(8,2) NOT NULL,
  email varchar(120) NOT NULL,
  PRIMARY KEY (id_funcionario)
);

DROP TABLE IF EXISTS matriculado;
CREATE TABLE matriculado (
  id_matriculado int NOT NULL AUTO_INCREMENT,
  fk_matricula int DEFAULT NULL,
  PRIMARY KEY (id_matriculado),
  KEY fk_matricula (fk_matricula),
  CONSTRAINT matriculado_ibfk_1 FOREIGN KEY (fk_matricula) REFERENCES alunos (matricula)
);

DROP TABLE IF EXISTS modalidades;
CREATE TABLE modalidades (
  ID int NOT NULL AUTO_INCREMENT,
  nome varchar(255) NOT NULL,
  duracao char(3) NOT NULL,
  PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS `personal`;
CREATE TABLE `personal` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `CREF` char(6) NOT NULL,
  `email` varchar(255) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `CPF` char(11) NOT NULL,
  PRIMARY KEY (`ID`)
);
