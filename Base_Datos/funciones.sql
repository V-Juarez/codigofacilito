DELIMITER // --- CREAR FUNCION, se a combiado el ; por //

CREATE FUNCTION agregra_dias(fecha DATE, dias INT)    --sentencias
RETURNS Date
BEGIN
  RETURN fecha + INTERVAL dias DAY;
END//

DELIMITER ; --volver a su funcion original ;
