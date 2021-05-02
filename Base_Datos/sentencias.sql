/*
Que tipo de entidades? autores
Nombre : autores
*/

/*Nombre
Genero
Fecha de nacimiento
Pais de origen

columna y el tipo de dato
*/

DROP DATABASE IF EXISTS libreria_cf;
CREATE DATABASE IF NOT EXISTS libreria_cf;

USE libreria_cf;

CREATE TABLE IF NOT EXISTS autores(
  autor_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, --NOT NULL  lave Primaria
  nombre  VARCHAR(25) NOT NULL,
  apellido VARCHAR(25) NOT NULL,
  seudonimo VARCHAR(50) NOT NULL,
  genero  ENUM ('M', 'F'),--CHAR(1),  --M o F
  fecha_nacimiento DATE NOT NULL,
  pais_origen VARCHAR(40) NOT NULL,
  fecha_creacion DATETIME DEFAULT current_timestamp
);

ALTER TABLE autores ADD COLUMN cantidad_libros INT DEFAULT 0;

CREATE TABLE libros(
  libro_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  autor_id INT UNSIGNED NOT NULL,
  titulo VARCHAR(50) NOT NULL,
  descripcion VARCHAR(250) NOT NULL DEFAULT '',
  paginas INTEGER UNSIGNED NOT NULL DEFAULT 0,
  fecha_publicacion DATE NOT NULL,
  fehca_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (autor_id) REFERENCES autores(autor_id)  ON DELETE CASCADE--tabla_referencia(llava_primaria)
);

CREATE TABLE libros_id(
  libro_id INT UNSIGNED NOT NULL,
  usuario_id INT UNSIGNED NOT NULL,

  FOREIGN KEY (libro_id) REFERENCES libros(libro_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE libros ADD ventas INT UNSIGNED NOT NULL DEFAULT 0,
ALTER TABLE libros ADD stock INT UNSIGNED DEFAULT 10;

--ALTER TABLE libros ADD FOREIGN KEY (autor_id) REFERENCES autores(autor_id)  ON DELETE CASCADE

INSERT INTO autores(autor_id, nombre, apellido, genero, fecha_nacimiento, pais_origen)
VALUES  (1, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (2, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (3, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (4, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (5, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (6, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');
        (7, 'Test autor', 'Test autor', 'M', '2020-05-17', 'Mexico');

INSERT INTO autores(nombre, apellido, seudonimo, fecha_nacimiento, genero, pais) --Al tener la llave primaria, el id ya no va al pincipio
  values('Stephen Edwin', 'King', 'Richard Bachman', '1947-09-07', 'M', 'USA');
        ('Joanne', 'Rowling', 'J.K Rowling', '1947-09-27', 'F', 'Reino Unido');

INSERT INTO libros(autor_id, titulo, fecha_publicacion)
    VALUES  (1, 'Carrie', '1974-01-01'),
            (1, 'El misterio de Salmes Lot', '1975-01-01'),
            (1, 'El resplando', '1977-01-01'),

            (2, 'Harry Potter y la Piedra Filosofal', '1997-06-30'),
            (2, 'Harry Potter y la Camara Secreta', '1998-07-02'),
            (2, 'Harry Potter y Prisionero de Azkaban', '1999-07-08'),
            (2, 'Harry Potter y el Caliz de Fuego', '2000-03-20'),
            (2, 'Harry Potter y la Orden de Fenix', '2003-06-21'),
            (2, 'Harry Potter y el Misterio del Principe', '2005-06-16'),
            (2, 'Harry Potter y las Reliquias de la Muerte', '2007-07-21');

VALUES (1, 'Carrie', '1974-01-01')

INSERT INTO libros (autor_id, titulo, fecha_publicacion)
VALUES  ('Eduardo', 'Garcia', 'eduardogpg', 'eduardo@codigofacilito.com'),
        ('Codi1', 'Facilito', 'codigofacilito', 'ayuda@codigofacilito.com');
        ('Codi2', 'Facilito', 'codigofacilito', 'ayuda@codigofacilito.com');
        ('Codi3', 'Facilito', 'codigofacilito', 'ayuda@codigofacilito.com');

INSERT INTO libros_usuarios(libro_id, usuario_id)
VALUES (1, 1), (3, 1), (3, 1),
        (55, 3), (55, 3), (55, 3);


--DESC autores;
--DESC libros;



SELEC * FROM libros WHERE  titulo IN ('Ojos de Fuego', 'Cujo', 'El hobbit'. 'La Torre Oscura 7 La Torre Oscura') --Busqued por listas


--DELETE FROM libros WHERE autor_id = 1;     -- Eliminar datos



--SELECT * FROM libros WHERE  titulo = "Ojos de fuego" OR   --Busqued por listas, de esta forma es es mas complicado ya que debenos agrergar 10 y muchas or.
  --                          titulo = "Cujo" OR
    --                        titulo = "El hobbit"  OR
      --                      titulo = "La Torre Oscura 7 La Torre Oscura";
--SELECT titulos, fecha_publicacion FROM libros
--WHERE fecha_publicacion BETWEEN '1995-01-01' AND '2015-01-01';      --Obtener rangos con Between

SELECT * FROM autores;
SELECT * FROM libros;
/*INSERT INTO autores(autor_id, nombre, apellido)
VALUES (1, 'Test autor', 'Test autor');*/
