START TRANSACTION;

SET @libro_id = 20, @usuario_id = 3,

UPDATE libros SET stock = stock - 1 WHERE libro_id = @libro_id;
SELECT stock FROM libros WHERE libro_id = @libro_id;

INSERT INTO libros_usuarios(libro_id, usuario_id) VALUES(@libro_id, @usuario_id);
SELECT * FROM libros_usuarios;


COMMIT;     --continuar con los datos actualizados
ROLLBACK;   --revertir un mensaje_error

--
DELIMITER //

CREATE PROCEDURE prestamo(usuario_id INT, libro_id INT)
BEGIN

  DECLARE EXIT SQLEXCEPTION  --Ocurre un mensaje_error
  BEGIN
    ROLLBACK;
  END;

  START TRANSACTION;

  INSERT INTO libros_usuarios(libro_id, usuario_id) VALUES(libro_id, usuario_id);
  UPDATE libros SET stock = stock - 1 WHERE libros.libros_id = libros_id;

  COMMIT;
  ROLLBACK;

END//
