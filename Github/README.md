

<h1>Tabla de Contenido</h1>

- [1. Introducción](#1-introducción)
	- [Qué es Git](#qué-es-git)
	- [Donde puedo usar control de versiones](#donde-puedo-usar-control-de-versiones)
	- [Git en el mundo](#git-en-el-mundo)
	- [GitHub/Gitlab](#githubgitlab)
	- [Instalación en Mac](#instalación-en-mac)
	- [Instalación en Windows](#instalación-en-windows)
	- [Instalar Git en GNU/Linux](#instalar-git-en-gnulinux)
	- [Nuevo proyecto - Identificarme](#nuevo-proyecto---identificarme)
- [2. Trabajo a nivel local con Git](#2-trabajo-a-nivel-local-con-git)
	- [Tres áreas en Git](#tres-áreas-en-git)
	- [Agregando archivos - Tracking Files](#agregando-archivos---tracking-files)
	- [Primeros commits y viajes en el tiempo](#primeros-commits-y-viajes-en-el-tiempo)
	- [RESET!](#reset)
	- [Qué son las ramas](#qué-son-las-ramas)
	- [Trabajo en Ramas](#trabajo-en-ramas)
- [3. Trabajando con GitHub](#3-trabajando-con-github)
	- [Trabajar con GitHub](#trabajar-con-github)
	- [GitHub begins](#github-begins)
	- [Subir un proyecto local a GitHub](#subir-un-proyecto-local-a-github)
	- [Fork de proyectos](#fork-de-proyectos)
	- [GitHub Teams](#github-teams)
	- [Todo sobre ISSUES](#todo-sobre-issues)
	- [Pull Request](#pull-request)
	- [Summary tercera unidad](#summary-tercera-unidad)
- [4. Clases en vivo](#4-clases-en-vivo)
	- [End to end projects with GitHub](#end-to-end-projects-with-github)


# 1. Introducción

## Qué es Git

Version de control de proyectos.


## Donde puedo usar control de versiones

Es ideal para trabajos colaborativos


## Git en el mundo

Hola, después de ver algunos vídeos presenciales sobre control de versiones y Git sería bueno que leyeras unas cuantas lineas acerca de lo que representa Git en el mundo del software, Git es usado por las grandes empresas, basicamente, es la herramienta que permite que muchas de las aplicaciones que usas hoy en día sean tal y como las conoces de esta forma, a continuación algunos ejemplos que podrás corroborar cuando visitemos la página de Git para descargarlo, pero de mientras, me gustaría mencionarte esta lista de grandes empresas emplean Git para su realización, seguramente conoces a casi todas.

	- Facebook
	- Twitter
	- Netflix
	- Google
	- LikedIn
	- 
Esas son por supuesto empresas que venden productos de Internet, usarlas es el pan de todos los días en estos tiempos, pero... y si te digo que Git influye en la creación no solo de aplicaciones, si no que también tiene presencia en los equipos de trabajo que desarrollan sistemas operativos para los dispositivos, tales como:

	- Microsoft
	- Android
	- LINUX

Incluso, el software que nos ayuda a crear más software, tales como sistemas de bases de datos, frameworks, IDE's también hacen uso de GIT! Algunos ejemplos:

	- Rails (Framework de Ruby para desarrollo web)
	- Postgres SQL (Sistema de base de datos)
	- Eclipse (Antiguo IDE para crear aplicaciones Android)áá

No cabe duda de que hay muchos ejemplos de equipos de trabajo que usan Git para trabajar, mejor no perdamos el tiempo y empecemos a aprender a usar Git para mejorar nuestra formación profesional como desarrolladores, no solo de software, si no de contenido y productos profesionales para hacer de este mundo un lugar mejor.


## GitHub/Gitlab

- [GitHub](https://githabo.com)
- [GitLab](https://gitlab.com)


## Instalación en Mac

Buscar `git` y descargar el archivo de instalacion.

## Instalación en Windows

Buscar `git` y descargar el archivo de instalacion.

## Instalar Git en GNU/Linux

Instalar `git` desde terminal
``` BASH
sudo apt-get install git
```

Hola, si estás leyendo este artículo es seguramente porque est´ás interesado en instalar Git en tu sistema operativo LINUX, y bueno, seamos honestos, si est´ás usando un sistema basado en LINUX es porque seguramente te llevas bien con los códigos y con las instalaciones en la terminal, pues bueno, entonces, decidí honrar tu gusto por las lineas de código de terminal y dejarte un tutorial muy sencillo de como instalar Git en tu LINUX Cabe mencionar que es muy sencillo, no te sorprendas de lo fácil que esto resulte. Abriremos nuestra terminal y actualizamos la lista de paquetes por si las moscas:

```bash
sudo apt-get update
sudo apt-get upgrade
```

y ahora si, instalamos Git:

```bash
apt-get install git
```

Como ves, es bastante sencillo el instalar Git en nuestros equipos LINUX, apartir de ahora, podrás trabajar el resto del curso sin problemas desde tu sistema operativo.

## Nuevo proyecto - Identificarme

``` BASH
# Name
git config --global user.name "Eduardo"

# email
git config --globla user.email "hola@example.com"
```

# 2. Trabajo a nivel local con Git

## Tres áreas en Git

	1. `Directorio de trabajo / Working Area:` Es la carpeta donde están alojados los archivos del proyecto.

	2. `Area de preparacion / Staging Area:` Es una zona intermedia. Es un archivo que almacena información acerca de lo que va a ir en tu próxima confirmación.

	3. `Git Area / .git directory:` Es la zona final, en ella se alberga el ultimo COMMIT hecho (osea el status actual del proyecto).


## Agregando archivos - Tracking Files

Crea un repositorio local.

```bash
git init 
```

Pregunta el status de nuestro repositorio.

```bash
git status 
```

Agrega archivos al Staging Area

```bash
git add . 
```

Agregar todos los archivos al Staging Area.

```bash
git add -A 
```

*nombre y extension del archivo*: Quita un archivo del Staging Area

```bash
git rm --cached 
```

## Primeros commits y viajes en el tiempo

Crear `commit`
``` BASH
git commit -m "mensaje | mi primer commit"
```

con `checkout` viajamos en el tiempo

```bash
# Viajamos a un commit en el tiempo
git checkout <id-commit>

# regresamos al ultimo commit
git checkout master
```

## RESET!

1. Reset soft: 

```bash
git reset --soft <id_commit>
```

Deja el commit, indicado en el comando, como último sin modificar el proyecto.

2. Reset hard: 

```bash
git reset --hard <id_commit>
```

Deja el commit, indicado en el comando, como último modificando el proyecto con las características de dicho commit.

## Qué son las ramas

Diferentes ramas, son espacios paralelos. Que dos o mas miembros pueden trabajar en la misma rama.

## Trabajo en Ramas

Crear rama
``` BASH
git branch pruebas

# Movernos en tre rma
git checkout pruebas

# Merge de ramas
git merge pruebas

# Eliminar rama
git branch pruebas -d
```

# 3. Trabajando con GitHub

## Trabajar con GitHub



## GitHub begins



## Subir un proyecto local a GitHub



## Fork de proyectos



## GitHub Teams



## Todo sobre ISSUES



## Pull Request



## Summary tercera unidad



# 4. Clases en vivo

## End to end projects with GitHub




Hola mundo desde git en codigo facilito.

Live de cofigo facilito de git, y que hacer para aprender git


------------- Configuracion git inicio -----------------

	git config --list

	git config --global

	git add --all
	
	git add .

	git commit -m "mensaje"


	git push orign <master> rama 

	git log


------------ ver datos en pantalla ----------------

	git log --graph 
	
	git log --oneline
	
	git commit --amend 
	
	git commit -- amend -m "Nuevo mensaje"

	git diff

	git difftool 

Etiquetas git tag newfolder number

	git checkout  -> moverse entre las ramas

	git checkout -b example2 -> creamos a nueva rama y/o commits

	git branch -m "example2" -> Renombrar las ramas

	
------------ crear una nueva rama -----------------

	  git switch -c nombre <nueva rama>

------------ en listar las ramas ------------------

	git branch	

	git branch --list


------------ hacer un merge ----------------------

	git merge example1

	git blame archivo -> nuestra los cambios realizados 

	git blame -L5,10 README.md

	git branch -D example1 -> elimina la rama

	git checkout -> movernos en las ramas
