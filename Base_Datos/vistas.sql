--CREATE VIEW prestamos_usuarios_vw AS
CREATE OR REPLACE VIEW prestamos_usuarios_vw AS
SELECT
  usuario.usuario_id,
  usuario.email,
  usuario.username,
  COUNT(usuarios.usuario_id) AS total_prestamos

FROM usuarios
INNER JOIN libros_usuarios ON usuarios.usuario_id = libros_usuarios.
            AND libros_usuarios.fehca_creacion >= CURDATE() - INTERVAL 5 DAY                  --editar vista
GROUP BY usuarios.usuario_id;
