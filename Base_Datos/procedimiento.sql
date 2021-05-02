DELIMITER //

CREATE PROCEDURE prestamos(usuario_id INT, libro_id INT, OUT cantidad INT)  -- out
BEGIN

  SET cantidad = (SELECT stock FROM libros WHERE libros.libro_id = libro_id);

  IF cantidad > 0 THEN

    INSERT INTO libros_usuarios(libros_id, usuario_id) VALUES(libro_id, usuario_id)
    UPDATE libros SET stock = stok - 1 WHERE libros.libro_id = libro_id

    SET cantidad = cantidad - 1;

    --ELSEIF condicion

    ELSE

    SELECT "No es posible realizar el prestamo" AS mensaje_error;

    END IF;

END//

CREATE PROCEDURE tipo_lector(usuario_id INT)
BEGIN

  SET @cantidad = (SELECT COUNT(*) FROM libros_usuarios
                    WHERE libros.usuarios.usuario_id = usuario_id);


--casos
CASE
  WHERE @cantidad > 20 THEN
    SELECT "Fanatico" AS mensaje;
  WHERE @cantidad > 10 AND @cantidad < 20 THEN
    SELECT "Aficionado" AS mensaje;
  WHERE @cantidad > 5 AND @cantidad < 10 THEN
    SELECT "Promedio" AS mensaje;
  ELSE
    SELECT "Nuevo" AS mensaje;
END CASE;

CREATE PROCEDURE  libros_azar()
BEGIN
  SET @iteracion = 0;

--  WHILE @iteracion < 5 DO
REPEAT

    SELECT libro_id, titulo FROM libros ORDER BY RAND() LIMIT 1;
    SET @iteracion = @iteracion + 1;

    UNTIL @iteracion >= 5
  END REPEAT;
--  END WHILE;

END //


DELIMITER ;
