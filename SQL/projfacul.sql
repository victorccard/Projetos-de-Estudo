CREATE TABLE CONTRATADO
(
    ID_JOGADOR  NUMBER(10,0) NOT NULL,
    DATA_INICIO DATE NOT NULL,
    DATA_FIM    DATE NOT NULL,
    CONSTRAINT PK_CONTRATADO PRIMARY KEY (ID_JOGADOR, DATA_INICIO),
    CONSTRAINT FK_CONTRATADO_REF_JOGADOR FOREIGN KEY (ID_JOGADOR)
        REFERENCES JOGADOR(ID_JOGADOR),
    CONSTRAINT CK_CONTRATADO CHECK (DATA_FIM > DATA_INICIO)    
);

ALTER TABLE CONTRATADOS RENAME TO CONTRATADO;

ALTER TABLE CONTRATADO ADD APELIDO VARCHAR2(30);

ALTER TABLE JOGADOR RENAME COLUMN APELIDO TO NICKNAME;

DESC JOGADOR;

ALTER TABLE JOGADOR MODIFY POSICAO NUMBER(5,0);

ALTER TABLE JOGADOR DROP COLUMN BI CASCADE CONSTRAINTS;

DROP TABLE JOGADOR; 

DROP CONSTRAINT FK_CONTRATADO_REF_JOGADOR;

DISABLE CONSTRAINT FK_CONTRATADO_REF_JOGADOR;