<h1>Docker</h1>

<h3>Luis Fernando Garcia</h3>

<h1>Tabla de Cotendio</h1>

- [1. Introduccion](#1-Introduccion)

# 1. Introduccion 

## Introducción a Docker

Docker es una plataforma completa de manejo de contenedores. A lo largo de este curso aprenderás qué es Docker, por qué usarlo y te introducirás en el manejo de dichos contenedores con ejemplos prácticos que te guían a través del mundo del manejo de aplicaciones con contenedores.

## Conceptos

Imagenes 
--

Contenedores
--

Docker hub
--

- [Docker Hub](https://hub.docker.com/)

## Instalación

- [Install Docker Engine](https://docs.docker.com/engine/install/)

Al finalizar la instalacion, concedemos permisos a docker para el usuario:

```bash
# Permisos
sudo usermod -aG docker 

# Estado de docker
docker ps -a
```

## Hola Mundo

```bash
# Descargar la imagen de docker
docker image pull fernando93d/hello

# maner imagenes de Docker
docker image 

# Listar las images 
docker image ls

# Ejecutar docker
dokcer container run fernando93d/hello 
```

# 2. Contenedores

## Comandos Básicos

Listar los contenedor

```bash
docker container ls

# Concer las funcionalidades de los comandos
docker container ls --help
docker container ls -a

➜  docker git:(master) ✗ docker container run fernando93d/hello
    __  __      __         __  ___                __
   / / / /___  / /___ _   /  |/  /_  ______  ____/ /___
  / /_/ / __ \/ / __ `/  / /|_/ / / / / __ \/ __  / __ \
 / __  / /_/ / / /_/ /  / /  / / /_/ / / / / /_/ / /_/ /
/_/ /_/\____/_/\__,_/  /_/  /_/\__,_/_/ /_/\__,_/\____/



➜  docker git:(master) ✗ docker container ls -a
CONTAINER ID   IMAGE               COMMAND             CREATED          STATUS                      PORTS     NAMES
11ee6a572fbe   fernando93d/hello   "python ./app.py"   42 seconds ago   Exited (0) 39 seconds ago             charming_wright
➜  docker git:(master) ✗


# Eliminar un contenedor
docker container rm --help
docker container rm id o <nombre>

# Corre docker
docker conatiner create fernando93d/hello

# Inciar contenedor
docker container start fernando93d/hello
```

## Modo Interactivo en Docker

Descargar contenedores

```bash
# Descargar contenedor
docker image pull ubuntu # versin le agregamos :latest o :rolling

docker image pull ubuntu:latest

# Descargar contenedor de nginx
docker image pull nginx

# ejecurar el contenedor
docker container run nginx

docker container run -d nginx # ejecutandose en segundo plano

# docker intercativo
docker container run -it ubuntu:latest

# salir del contenedor
exit

# contenedor en segundo plano
docker container run -itd ubuntu

```


## Ejecutar comandos dentro de un contenedor

execute exe = ejecutar 

```bash
# insteracion con la terminal del contenedor
docker container attach id-container

# exec mantener el contenedor acitvo
docker container run -itd ubuntu

docker container exec id ls

# Interaccion de terminal del contenedor
docker container exec -it id bash

# top -> ver los procesos
docker container top id 

# Detener contenedor
docker stop id

# Listamos los contenedores
docker ps -a
```

## Puertos

```bash
# nginx
docker container run -d nginx

# Detener contenedor
docker stop id

# lista los contenedores acitvos
docker container ls -q

# detener todos los contendores
docker container stop $(docker container ls -q)

# remor los contenedor apagados
docker container prune
```

Puertos

```bash
# activar nginx en el puerto 80:80 agregando -p
docker git:(master) ✗ docker conatiner run -d -p 80:80 nginx

# activar otro puerto
➜  docker git:(master) ✗ docker container run -d -p 8080:80 nginx

# realizamos 
curl localhost

# ver en que puerto esta el contenedor
➜  docker git:(master) ✗ docker container port id

# pueto aleatorio
➜  docker git:(master) ✗ docker container run -d -P nginx
```

## Logs

Logs es para verificar que el contenedor se a ejecutado exitosamente

```bash
docker container logs id 

# Descagar el contenedor de mysql
docker image pull mysql

# Ejecutar en segundo plano
docker container run -d mysql

# listar los contenedor ejecutandose
docker container ls -a

# Ver el error 
docker container logs id
```

## Commits

```bash
docker container run -dit ubunut

# exec
docker container exec -it id bash

# Creamos el archivo data.txt
touch data.txt

# crear commit con el id <nombre>
docker container commit id ubuntu-file

# copiamos el nombre y ejecutamos un nuevo contenedor
docker container run -it ubuntu-file

➜  ~ docker container run -it 38d09fc700fd
root@58d909ebd20d:/# ls
bin  boot  data.txt  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@58d909ebd20d:/#
```

# 3. Volumenes

Overview Volúmenes
Creando Volúmenes
Compartiendo archivos con contenedores

# 4. Imagenes

Overview Imágenes
Dockerfile
Copiar archivos
Variables de entorno
Argumentos
Dockerignore
Trabajando con usuarios
Ejecutando comandos CMD
CMD VS ENTRYPOINT
Contenerizar app
Subir imagen al docker hub

# 5. Redes

Redes en Docker
Inspeccionado redes
Creando redes
Agregando Ip estática a contenedor

# 6. Docker Machine

Overview docker machine
Creando máquina digitalocean
Accediendo al docker machine

# 7. Docker Compose

Docker compose overview
Servicios
Variables de entorno
Redes
Volúmenes

# 8. Orquestadores

Orquestadores teoría
Docker swarm
Docker swarm deploy servicio
Docker swarm actualizar puertos
Kubernetes conceptos
Kubernetes en local minikube

#9. Extras

Compartiendo dispositivos con el contenedor
Docker api
Proxy reversivo

#10. Clases en vivo
Clase en Vivo: Primeros pasos en Docker
Tecnologías Devops

