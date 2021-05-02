--consulta
SELECT CONCAT(nombre, " ", apellido) AS nombre_completo "", pais_origen AS email FROM autores
UNION
SELECT CONCAT(nombre, " ", apellidos) AS nombre_completo, email, "" FROM usuarios;


--sub Consultas

SELECT AVG(ventas) FROM libros; --320.1818

SELECT CONCAT(nombre, "", apellido) AS nombre
FROM autores
WHERE autor_id IN(
  SELECT                                                  --SET @promedio = (SELECT AVG(ventas) FROM libros);
    autor_id
  FROM libros
  GROUP BY autor_id
  HAVING SUM(ventas) > (SELECT AVG(ventas) FROM libros)); --Obtener @promedio EN SUBCONSULTA

--validar registros de consultas, ser cuidados con que campo hay que trabajar.
Disponible
No Disponible
El hobbit

SELECT IF(
  EXISTS(SELECT libro_id FROM libros WHERE titulo = 'El hobbit'),
  'Disponible',
  'No Disponible'
) AS mensaje;
