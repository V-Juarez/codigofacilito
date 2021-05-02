DELIMITER //

CREATE TRIGGER after_insert_actaulizacion_libros      --CREAR UN TRIGGER
AFTER INSET ON libros
FOR EACH ROW
BEGIN
  UPDATE autores SET cantidad_libros = cantidad_libros + 1 WHERE autor_id = NEW.autor_id;
END;
//

--TRIGGER PARA ELIMINAR REGISTROS DE libros
CREATE TRIGGER after_delete_actualizacion_libros
AFTER DELETE ON libros
FOR EACH ROW
BEGIN
  UPDATE autores SET cantidad_libros = cantidad_libros - 1  WHERE autor_id = OLD.autor_id;
END;


--cambiar de autor y libro, el cual decresera al ser cambiado

CREATE TRIGGER after_update_actualizacion_libros
AFTER UPDATE ON libros
FOR EACH ROW
BEGIN

  IF(NEW.autor_id != OLD.autor_id) THEN
    UPDATE autores SET cantidad_libros = cantidad_libros + 1 WHERE autor_id = NEW.autor_id;
    UPDATE autores SET cantidad_libros = cantidad_libros - 1 WHERE autor_id = OLD.autor_id;

    END IF;
END;
//

DELIMITER ;
