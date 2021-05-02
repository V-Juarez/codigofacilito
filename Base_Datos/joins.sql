--JOIN
SELECT
  li.titulo
  CONCAT(au.nombre, " ", au.apellido) AS nombre_completo,
  li.fehca_creacion
FROM libros AS li
INNER JOIN autores AS au ON li.autor_id = au.autor_id;

--sub clausulas using
SELECT
  libors.titulo
  CONCAT(autores.nombre, " ", autores.apellido) AS nombre_completo,
  libros.fehca_creacion
FROM libros
INNER JOIN autores  ON libros.autor_id = autor.autor_id
            AND autores.seudonimo IS NOT NULL;            --ON->Condicionar mas columnas USING->NO es posible hacer lo de condicionar mas columnas

--left JOIN
LEFT JOIN  --usuarios libros De muchos a muchos

CREATE TABLE libros_id(
  libro_id INT UNSIGNED NOT NULL,
  usuario_id INT UNSIGNED NOT NULL,

  FOREIGN KEY (libro_id) REFERENCES libros(libro_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

--tablas a, b

usuarios = a
libros_usuarios = b

SELECT
  CONCAT(nombre, " ", apellidos)
  libros_usuarios.libros_id
FROM usuarios
LEFT JOIN libros_usuarios ON usuarios.usuarios_id = libros_usuarios.usuario_id
WHERE libros_usuarios.libro_id IS NULL;

--RIGHT JOIN
libros_usuarios = a
usuarios = b

SELECT
  CONCAT(nombre, " ", apellidos)
  libros_usuarios.libros_id
FROM libros_usuarios
RIGHT JOIN libros_usuarios ON usuarios.usuarios_id = libros_usuarios.usuario_id
WHERE libros_usuarios.libro_id IS NULL;


--MULTIPLES JOINS
usuarios
libros_usuarios
libros
autores

SELECT
  CONCAT(usuarios.nombre, " ", usuarios.apellidos) AS nombre_usuario
FROM usuarios
INNER JOIN libros_usuarios ON usuarios.usuario_id = libros_usuarios.usuario_id
            AND DATE(libros_usuarios.fecha_creacion) = CURDATE()
INNER JOIN libros ON libros_usuarios.libro_id = libros.libro_id
INNER JOIN autores ON libros.autor_id = autores.autor_id
            AND autores.seudonimo IS NOT NULL;

      --Productos Cartecianos
