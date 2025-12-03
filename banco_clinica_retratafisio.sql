CREATE DATABASE clinica_retratafisio;

USE clinica_retratafisio;

CREATE TABLE Alunos ( 
ID_Aluno int not null auto_increment , 
Nome_Aluno varchar (50) not null ,
Data_Nascimento_Aluno date , 
CPF_Aluno int not null , 
Endereco_Aluno varchar (50), 
Telefone_Aluno numeric (11) , 
Telefone_Emergencia_Aluno numeric (11),
primary key (ID_Aluno));

ALTER TABLE Alunos
modify column Data_Nascimento_Aluno varchar(10);

ALTER TABLE Alunos
modify column CPF_Aluno varchar(11);

ALTER TABLE Alunos
add column Email_Aluno varchar(50);

CREATE TABLE Pacientes ( 
ID_Paciente int not null auto_increment , 
Nome_Paciente varchar (50) not null , 
Data_Nascimento_Paciente date , 
CPF_Paciente int not null , 
Endereco_Paciente varchar (50) , 
Telefone_Paciente numeric(11) ,
Telefone_Emergencia_Paciente numeric(11),
primary key (ID_Paciente)); 

ALTER TABLE Pacientes
modify column Data_Nascimento_Paciente varchar(10);

ALTER TABLE Pacientes
modify column CPF_Paciente varchar(11);

ALTER TABLE Pacientes
add column Email_Paciente varchar(50);

CREATE TABLE Turmas ( 
ID_Turma int not null auto_increment , 
Turma_Manha varchar (50) , 
Turma_Tarde varchar (50) ,
Turma_Noite varchar (50) , 
Data_Turma date , 
Hora_Turma time ,
primary key (ID_Turma) , 
ID_Aluno int,
foreign key (ID_Aluno) references Alunos(ID_Alunos)) ; 

CREATE TABLE Consultas ( 
ID_Consulta int not null auto_increment , 
Data_Consulta date , 
Hora_Consulta time , 
primary key (ID_Consulta) , 
ID_Paciente int , 
foreign key (ID_Paciente) references Pacientes(ID_Paciente)) ; 

CREATE TABLE Servicos ( 
ID_Servico int not null auto_increment , 
Nome_Servico varchar (50) , 
Preco_Servico float , 
primary key (ID_Servico)); 

CREATE TABLE Agendamentos ( 
ID_Agendamentos int not null auto_increment , 
Data_Agendamento date , 
Hora_Agendamento time , 
primary key (ID_Agendamentos)); 

CREATE TABLE IF NOT EXISTS Perfis ( 
ID_Perfil int not null auto_increment , 
Nome_Perfil varchar (100), 
primary key (ID_Perfil)); 

CREATE TABLE Usuarios ( 
ID_Usuario int not null auto_increment ,
Usuario varchar (50) ,
Senha varchar (50) ,
primary key (ID_Usuario)) ;

#Adicionando o ID_Perfil na tabela Usuarios
ALTER TABLE Usuarios
ADD COLUMN ID_Perfil int;

ALTER TABLE Usuarios
ADD COLUMN Nome varchar(100) not null ; 

#Adicioando ID_Peril como chave estrangeira na tebela Usuarios
ALTER TABLE Usuarios
ADD CONSTRAINT fk_perfil
FOREIGN KEY (ID_Perfil) references Perfis (ID_Perfil); 

INSERT INTO Perfis ( Nome_Perfil ) VALUES ('Administrador') , ('Usuário Comun');

INSERT INTO Usuarios ( Usuario , Senha ) 
VALUES 
( 'Joao' , '12345' ),
('Admin', '25520');


