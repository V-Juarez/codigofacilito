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
source venv/bin/actvate
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

Render template 

Se utiliza de esta manera:

```py
@app.route('/contacto')
def contacto():
  data={
      'titulo':'Contacto',
          'encabezado':'Bienvenidos(a)'
            }
              return render_template('contacto.html', data=data) # render template
```


## Archivos estáticos

Los archivos estaticos son `.html`, en la carptea  `templates`,  `.css`, en la carpeta `static/css`, `.js`, en la carpeta `static/js`
por convencion los documentos deben ser guardados en cada carpeta corespondiente.

Puedes utilizar  un archivo normal, pero en esta ocasion y porque jinja, lo permite. Utilizaremos plantillas.

como principal archivo `hmtl` sera `base.html`.

```html
<!-- utilizamos contenido de nuestra plantilla y es de esta manera como llamamos nuestros archivos css, js y html  -->
<title>{{ data.titulo }}</title>
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">

<script src="{{ url_for('static', filename='js/index.js') }}"></script>
```



## Herencia de plantillas

La herencia de plantilla nos permitira crear y enlazar nuestros archivos `.html`

jinja nos permite utilizarlo de la siguiente manera

```html
{% extends './base.html' %} # Llamamos al archivo

{% block contenido %}    <!-- sintaxis de jinja, inivio -->

<p>
  Estmos en la seccion de Contacto   <!--html -->
  </p>

  {% endblock %}
  <!-- cierre de jinja -->
```


## Hipervínculos (links)

Crear `navbar`

```html
<a href="{{ url_for('index') }}">Index</a>
<a href="{{ url_for('contacto') }}">Contacto</a>
```

## Dinamismo en páginas web

Crear parametro y establecerlo. Para personalizarlo

```py
@app .route('/saludo/<nombre>')
def saludo(nombre):
  return 'Hola, {0}'.format(nombre)
```

Vamos a al navegar in escribimos 

`http://127.0.0.1:5005/saludo/123`

para ver lo dinamico de la pagina, escribiendo `/saludo/` luego en `nombre`.

O si queremos hacer una suma

escribiriamos en el navegar `localhost://suma/14/23` de esta forma `http://127.0.0.1:5005/suma/14/23`

Rutas dinamicas 

```py
@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
  return 'Tu nombre es: {0} y tu edad es: {1}'.format(nombre, edad)
```

## Paso de parámetros mediante URL

```py
@app.route('/lenguajes')
def lenguajes():
  data={
    'hay_lenguajes': True,
    'lenguajes':['PHP', 'Python', 'Kotlin', 'Rust', 'Java', 'C#', 'JavaScript']
  }
  return render_template('lenguajes.html', data=data)
```

Estructura de `lenguajes.html` con jinga con la condicion if y for.

```html
{% extends './base.html' %}

{% block contenido %}
<ul>

  {% if data.lenguajes|length > 0 %}

  {% for leng in data.lenguajes %}
  <li>{{  leng  }}</li>
  {% endfor %}

  {% else %}

  <h2>No hay lenguajes listados...</h2>
  
  {% endif %}

</ul>

{% endblock %}
```

## Query String

- `GET`
- `POST`
- `PUT`
- `DELETE`

```py
@app.route('/datos')
def datos():
  print(request.args)
  # valor1=request.args.get('valor1')
  a = request.args.get('valor1')
  b = int(request.args.get('valor2'))
  return 'Estos son los datos: {0}, {1}'.format(a, (b+15))
```

## Callbacks: Métodos antes y despúes de las peticiones

```py
# Antes de la peticion
@app.before_request
def before_request():
  print('Antes de la peticion...')

  # Despues de la peticion 
@app.after_request
def after_request(response):
  print('Despues de la peticion...')
  return response

  #Peticion
def index():
  print('Estamos accediendo a la peticion...')

```

# 2. Estructura del proyecto

## Estructura base del proyecto

Crear nuestra carpeta tienda, con las siguientes carpetas

  - app
    - templates
    - static


## Creación de entorno virtual para el proyecto

Instarlar nuestro entorno virtual 

```bash 
python3 -m venv venv

# Instalar flask
pip install flask

# Actualizar pip recomendable, el terminal nos sugiere hacerlo  correctamente copiamos el comando.

# Instalar flask-script
```

Crear nuestro archivo `__init__.py`

```py
from flask import Flask

app = Flask(__name__)


def inicializar_app():
    return app
```

Luego crear el archivo `manager.py` script para inicialir el proyecto, fuera del directorio `app`

```py
from flask_script import Manager
from app import inicializar_app

app = inicializar_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

Corremos el servidor con el siguiente comando

```bash
python manager.py runserver
```

Creamos nuestra primera vista en `__init__.py`

```py
@app.route('/')
def index():
    return 'Hola mundo!!!'
```

## Archivo de configuración del proyecto

Crear el archivo `config.creación-de-carpeta-y-estructura-de-plantillas`

## Manejo de error 404

Crear en el directorio `remplates/errores/404.html`
- [25 HTML Funny 404 Pages | Free Frontend](https://freefrontend.com/html-funny-404-pages/)


Crear el archivo `404.html`


importar la ruta en `__init__.py`
```py
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
```


## Creación de carpeta y estructura de plantillas

Crear nuestra base en el archivo `base.html` que con jinja, vamos a utilizar como plantilla.

Para utilizar jinja `{% %}` para refernciar que se esta utilizando como plantilla.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %} {% endblock %}</title>
  
  {% block customCSS %}
  {% endblock %}
</head>
<body>
  {% block body %}

  {% endblock %}

  {% block customJS%}
  {% endblock %}

</body>
</html>
```

Archivo `body.html`

```html
{% extends './base.html' %}

{% block body %}

{%  block container %}

{% endblock %}

{% endblock %}
```

## Integrando Bootstrap vía CDN

- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

Copiar los enlaces `css` y `javascript`

## Descarga e integración de Bootstrap

- [codigofacilito | primera-app-flask](https://github.com/codigofacilito/primera-app-flask)

# 3. Trabajo con formularios

## Formulario de inicio de sesión

Crear el archivo `login.html` en el directorio template y `login.css` en template/static.

Exportar el `link` utilizando jinja

```html
  {% block customCSS %}
  <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}">
  {% endblock %}
```

Imagenes con jinja

```bash
<header>
    <h1>{{ error }}</h1>
    <img src="{{ url_for('static', filename='img/404.gif') }}" />
  </header>
```

## Métodos HTTP aplicables

- `POST`
- `GET`
- `DELETE`
- ``

## Lectura de valores enviados desde formularios

Al ingresar las credenciales el usuario redirigirlos a index, datos incorrectos mostrarle nuevamente
`login.html`

## CSRF (Cross Site Request Forgery)

CSRF Cross-site Request Forgery: Solicitud de falsificacion entre sitios.

```bash
pip install Flask-WTF
```

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
