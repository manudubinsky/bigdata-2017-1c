--PASOS PARA INSTALAR LA LIBRERIA Y POSTGRES
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev


--PASOS PARA CONECTARSE

sudo su postgres
psql
alter user postgres password 'undav';
create database prueba;
\connect prueba

--COPIAR Y PEGAR O COMENTAR LO ANTERIOR Y EJECUTAR EL ARCHIVO
CREATE TABLE categoria(

    id_categoria serial NOT NULL,
    nombre varchar(200) NOT NULL  
);

CREATE TABLE articulo(
    id_categoria int NOT NULL,
    titulo text NOT NULL,
    id_articulo int NOT NULL 
);

CREATE TABLE articulo_autor(
    id_articulo int NOT NULL,
    id_autor int NOT NULL,
    PRIMARY KEY(id_autor,id_articulo)
);

CREATE TABLE autor_universidad(
    id_autor int NOT NULL,
    id_universidad int NOT NULL,
    PRIMARY KEY(id_autor,id_universidad)
    
);

CREATE TABLE autor(
    id_autor serial NOT NULL,
    mail text NOT NULL
);

CREATE TABLE universidad(
    id_universidad serial NOT NULL,
    provincia text NOT NULL
);

ALTER TABLE ONLY universidad
    ADD CONSTRAINT pk_universidad PRIMARY KEY (id_universidad);
    
ALTER TABLE ONLY autor
    ADD CONSTRAINT pk_autor PRIMARY KEY (id_autor);

ALTER TABLE ONLY categoria
    ADD CONSTRAINT pk_categoria PRIMARY KEY (id_categoria);
    
ALTER TABLE ONLY articulo
    ADD CONSTRAINT pk_articulo PRIMARY KEY (id_articulo);
    
ALTER TABLE ONLY articulo
    ADD CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria);
    
ALTER TABLE ONLY articulo_autor
    ADD CONSTRAINT fk_articulo FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo);

ALTER TABLE ONLY articulo_autor
    ADD CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES autor(id_autor);
    
ALTER TABLE ONLY autor_universidad
    ADD CONSTRAINT fk_universidad FOREIGN KEY (id_universidad) REFERENCES universidad(id_universidad);
    
ALTER TABLE ONLY autor_universidad
    ADD CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES autor(id_autor);

\dt

