SELECT  COUNT(*) FROM autores;

SELECT COUNT(*) AS total FROM autores WHERE seudonimo IS NOT NULL; --Obtener los seudonimo

SELECT COUNT(seudonimo) AS total FROM autores;    --Obtener seudonimos
