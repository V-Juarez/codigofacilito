<h1></h1>

<h3></h3>

<h1>Tabla de Contenido</h1>

- [1. Fundamentos](#1-fundamentos)
  - [Introducción al curso](#introducción-al-curso)
  - [Conocimientos previos](#conocimientos-previos)
  - [Qué es un framework y qué es Flask](#qué-es-un-framework-y-qué-es-flask)
  - [Entorno virtual de desarrollo e instalación](#entorno-virtual-de-desarrollo-e-instalación)
  - [Primer servidor con Flask](#primer-servidor-con-flask)
  - [Primera página web y hola mundo](#primera-página-web-y-hola-mundo)
  - [Render de templates](#render-de-templates)
  - [Archivos estáticos](#archivos-estáticos)
  - [Herencia de plantillas](#herencia-de-plantillas)
  - [Hipervínculos (links)](#hipervínculos-links)
  - [Dinamismo en páginas web](#dinamismo-en-páginas-web)
  - [Paso de parámetros mediante URL](#paso-de-parámetros-mediante-url)
  - [Query String](#query-string)
  - [Callbacks: Métodos antes y despúes de las peticiones](#callbacks-métodos-antes-y-despúes-de-las-peticiones)
- [2. Estructura del proyecto](#2-estructura-del-proyecto)
  - [Estructura base del proyecto](#estructura-base-del-proyecto)
  - [Creación de entorno virtual para el proyecto](#creación-de-entorno-virtual-para-el-proyecto)
  - [Archivo de configuración del proyecto](#archivo-de-configuración-del-proyecto)
  - [Manejo de error 404](#manejo-de-error-404)
  - [Creación de carpeta y estructura de plantillas](#creación-de-carpeta-y-estructura-de-plantillas)
  - [Integrando Bootstrap vía CDN](#integrando-bootstrap-vía-cdn)
  - [Descarga e integración de Bootstrap](#descarga-e-integración-de-bootstrap)
- [3. Trabajo con formularios](#3-trabajo-con-formularios)
  - [Formulario de inicio de sesión](#formulario-de-inicio-de-sesión)
  - [Métodos HTTP aplicables](#métodos-http-aplicables)
  - [Lectura de valores enviados desde formularios](#lectura-de-valores-enviados-desde-formularios)
  - [CSRF (Cross Site Request Forgery)](#csrf-cross-site-request-forgery)
  - [Validaciones en formularios HTML](#validaciones-en-formularios-html)
- [4. Integracion con bsse de datos](#4-integracion-con-bsse-de-datos)
  - [Creación de BD en MariaDB](#creación-de-bd-en-mariadb)
  - [Relaciones foráneas](#relaciones-foráneas)
  - [Inserción de registros en base de datos](#inserción-de-registros-en-base-de-datos)
  - [Configuración de conexión en Flask](#configuración-de-conexión-en-flask)
  - [Prueba de conexión hacia BD](#prueba-de-conexión-hacia-bd)
  - [Creación de entidades y modelos](#creación-de-entidades-y-modelos)
- [5. Gestion de sesiones](#5-gestion-de-sesiones)
  - [Gestión y encriptado de contraseñas](#gestión-y-encriptado-de-contraseñas)
  - [Inicio de sesión](#inicio-de-sesión)
  - [Trabajo con sesiones](#trabajo-con-sesiones)
  - [Cerrar sesión](#cerrar-sesión)
  - [Mensajes flash](#mensajes-flash)
  - [Archivo de constantes](#archivo-de-constantes)
  - [Categorías de mensajes flashed](#categorías-de-mensajes-flashed)
  - [Login requerido en URLs](#login-requerido-en-urls)
  - [Obtener sesión actual](#obtener-sesión-actual)
- [6. Operaciones con tablas](#6-operaciones-con-tablas)
  - [Operaciones para control de sesiones](#operaciones-para-control-de-sesiones)
  - [Listado de libros disponibles](#listado-de-libros-disponibles)
  - [Manejo de errores](#manejo-de-errores)
  - [Compra de libros, utilizando Fetch API](#compra-de-libros-utilizando-fetch-api)
  - [Perfeccionando el proceso de compra](#perfeccionando-el-proceso-de-compra)
  - [Listado de libros comprados en la página principal](#listado-de-libros-comprados-en-la-página-principal)
  - [Reporte de libros vendidos](#reporte-de-libros-vendidos)
- [7. Envio de emails](#7-envio-de-emails)
  - [Configuración del servidor de correos](#configuración-del-servidor-de-correos)
  - [Envío de correo de confirmación de compra](#envío-de-correo-de-confirmación-de-compra)
  - [Envío asíncrono de correos](#envío-asíncrono-de-correos)
- [8. extras](#8-extras)
  - [Creación de repositorio con Git](#creación-de-repositorio-con-git)
  - [Configuración de .gitignore](#configuración-de-gitignore)


# 1. Fundamentos
## Introducción al curso




## Conocimientos previos





## Qué es un framework y qué es Flask

Flask es un Framework

- [Flask | Documentation](https://flask.palletsprojects.com/en/1.1.x/)

## Entorno virtual de desarrollo e instalación

Instalar el entorno virtual

```bash
python3 -m venv ven
```

Activar entorno virtual

```bash
source venv./bin/actvate
```

Desactivar el entorno virtual

```bash
deactivate
```

En windows activar el entorno virutal

```bash
directorio .\env\Script\activate
```

Instalar flask

```bash
pip install flask
```

Listar los paquetes 

```bash
pip list
```

## Primer servidor con Flask

```py
from flask import Flask

app = Flask(__name__)



if __name__ == '__main__':
  app.run()
```

Correr el servidor

```bash
python app/app.py

# Detener el servidor
Ctl + c
```

## Primera página web y hola mundo

Crear una ruta de acceso para el servidor:

```py
"""
@app.route('/')
def index():
  return "CodigoFacilito"
"""

def index():
  return "Bienvenidos a CodigoFacilito"

@app.route('/holaMundo')
def hola_mundo():
  return "Hola Mundo! Desde codigofacilito"
```

```py
if __name__ == '__main__':
  app.add_url_rule('/',view_func=index)   # Funcion de flask para manterner la direccion principal
  app.run(debug=True, port=5005)   # Mantener el servidadr activo y actulizandose, cambiar de port
```

## Render de templates




## Archivos estáticos




## Herencia de plantillas




## Hipervínculos (links)




## Dinamismo en páginas web




## Paso de parámetros mediante URL




## Query String




## Callbacks: Métodos antes y despúes de las peticiones





# 2. Estructura del proyecto

## Estructura base del proyecto



## Creación de entorno virtual para el proyecto



## Archivo de configuración del proyecto



## Manejo de error 404



## Creación de carpeta y estructura de plantillas



## Integrando Bootstrap vía CDN



## Descarga e integración de Bootstrap



# 3. Trabajo con formularios
## Formulario de inicio de sesión
## Métodos HTTP aplicables
## Lectura de valores enviados desde formularios
## CSRF (Cross Site Request Forgery)
## Validaciones en formularios HTML
# 4. Integracion con bsse de datos
## Creación de BD en MariaDB
## Relaciones foráneas
## Inserción de registros en base de datos
## Configuración de conexión en Flask
## Prueba de conexión hacia BD
## Creación de entidades y modelos
# 5. Gestion de sesiones
## Gestión y encriptado de contraseñas
## Inicio de sesión
## Trabajo con sesiones
## Cerrar sesión
## Mensajes flash
## Archivo de constantes
## Categorías de mensajes flashed
## Login requerido en URLs
## Obtener sesión actual
# 6. Operaciones con tablas 
## Operaciones para control de sesiones
## Listado de libros disponibles
## Manejo de errores
## Compra de libros, utilizando Fetch API
## Perfeccionando el proceso de compra
## Listado de libros comprados en la página principal
## Reporte de libros vendidos
# 7. Envio de emails
## Configuración del servidor de correos
## Envío de correo de confirmación de compra
## Envío asíncrono de correos

# 8. extras
## Creación de repositorio con Git
## Configuración de .gitignore
