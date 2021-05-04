<h1>Docker</h1>

<h3>Luis Fernando Garcia</h3>

<h1>Tabla de Cotendio</h1>

- [1. Introduccion](#1-introduccion)
  - [Introducción a Docker](#introducción-a-docker)
  - [Conceptos](#conceptos)
  - [Imagenes](#imagenes)
  - [Contenedores](#contenedores)
  - [Docker hub](#docker-hub)
  - [Instalación](#instalación)
  - [Hola Mundo](#hola-mundo)
- [2. Contenedores](#2-contenedores)
  - [Comandos Básicos](#comandos-básicos)
  - [Modo Interactivo en Docker](#modo-interactivo-en-docker)
  - [Ejecutar comandos dentro de un contenedor](#ejecutar-comandos-dentro-de-un-contenedor)
  - [Puertos](#puertos)
  - [Logs](#logs)
  - [Commits](#commits)
- [3. Volumenes](#3-volumenes)
  - [Overview Volúmenes](#overview-volúmenes)
  - [Creando Volúmenes](#creando-volúmenes)
  - [Compartiendo archivos con contenedores](#compartiendo-archivos-con-contenedores)
- [4. Imagenes](#4-imagenes)
  - [Overview Imágenes](#overview-imágenes)
  - [Dockerfile](#dockerfile)
  - [Copiar archivos](#copiar-archivos)
  - [Variables de entorno](#variables-de-entorno)
  - [Argumentos](#argumentos)
  - [Dockerignore](#dockerignore)
  - [Trabajando con usuarios](#trabajando-con-usuarios)
  - [Ejecutando comandos CMD](#ejecutando-comandos-cmd)
  - [CMD VS ENTRYPOINT](#cmd-vs-entrypoint)
  - [Contenerizar app](#contenerizar-app)
  - [Subir imagen al docker hub](#subir-imagen-al-docker-hub)
  - [Para subir un contemedor a docker hub](#para-subir-un-contemedor-a-docker-hub)
- [5. Redes](#5-redes)
  - [Redes en Docker](#redes-en-docker)
  - [Inspeccionado redes](#inspeccionado-redes)
  - [Creando redes](#creando-redes)
  - [Agregando Ip estática a contenedor](#agregando-ip-estática-a-contenedor)
- [6. Docker Machine](#6-docker-machine)
  - [Overview docker machine](#overview-docker-machine)
  - [Creando máquina digitalocean](#creando-máquina-digitalocean)
  - [Accediendo al docker machine](#accediendo-al-docker-machine)
- [7. Docker Compose](#7-docker-compose)
  - [Docker compose overview](#docker-compose-overview)
  - [Servicios](#servicios)
  - [Variables de entorno](#variables-de-entorno-1)
  - [Redes](#redes)
  - [Volúmenes](#volúmenes)
- [8. Orquestadores](#8-orquestadores)
  - [Orquestadores teoría](#orquestadores-teoría)
  - [Nodos](#nodos)
  - [Swarm](#swarm)
  - [Servicios](#servicios-1)
  - [Tareas](#tareas)
  - [Docker swarm](#docker-swarm)
  - [Docker swarm deploy servicio](#docker-swarm-deploy-servicio)
  - [Docker swarm actualizar puertos](#docker-swarm-actualizar-puertos)
  - [Kubernetes conceptos](#kubernetes-conceptos)
  - [Kubernetes en local minikube](#kubernetes-en-local-minikube)
- [9. Extras](#9-extras)
  - [Compartiendo dispositivos con el contenedor](#compartiendo-dispositivos-con-el-contenedor)
  - [Docker api](#docker-api)
  - [Proxy reversivo](#proxy-reversivo)
- [10. Clases en vivo](#10-clases-en-vivo)
  - [Clase en Vivo: Primeros pasos en Docker](#clase-en-vivo-primeros-pasos-en-docker)
  - [Tecnologías Devops](#tecnologías-devops)

# 1. Introduccion 

## Introducción a Docker

Docker es una plataforma completa de manejo de contenedores. A lo largo de este curso aprenderás qué es Docker, por qué usarlo y te introducirás en el manejo de dichos contenedores con ejemplos prácticos que te guían a través del mundo del manejo de aplicaciones con contenedores.

## Conceptos

Imagenes 
---

Contenedores
---

Docker hub
---

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

## Overview Volúmenes



## Creando Volúmenes

```bash
# Volume - guarda la informacion en el disco duro
# creamos el Volumenes
docker volume create local

# listamos los volumens
docker volumen ls
DRIVER    VOLUME NAME
local     3622cb49156b6681a9efb233bac5de587a828cb16bda46dc24d75a66ba524aa1
local     local

# Inspeccionamos los volumens locales
➜  docker git:(master) ✗ docker volume inspect local
[
    {
        "CreatedAt": "2021-05-02T20:02:51-06:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/local/_data", # ubicacion
        "Name": "local",
        "Options": {},
        "Scope": "local"
    }
]
➜  docker git:(master) ✗

# montar el volumen /app
➜  docker git:(master) ✗ docker container run -dit -v local:/app victorgame/ubuntu
c4ce0941a3f40617b7b2ed90712867d682039ce16f7c2a0d1db562d733558c9d
➜  docker git:(master) ✗

# Creamos archivos en el contenedor
➜  docker git:(master) ✗ docker container exec -it c4ce0941a3f40617b7b2ed90712867d682039ce16f7c2a0d1db562d733558c9d bash
root@c4ce0941a3f4:/# ls
app  bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@c4ce0941a3f4:/# cd app
root@c4ce0941a3f4:/app# ls
root@c4ce0941a3f4:/app# touch a b c
root@c4ce0941a3f4:/app# ls
a  b  c
root@c4ce0941a3f4:/app# exit
exit

# listamos
➜  docker git:(master) ✗ docker ps -a
CONTAINER ID   IMAGE               COMMAND                  CREATED             STATUS                         PORTS                                     NAMES
c4ce0941a3f4   victorgame/ubuntu   "/bin/bash"              2 minutes ago       Up 2 minutes                                                             sharp_roentgen
58d909ebd20d   38d09fc700fd        "/bin/bash"              24 minutes ago      Up 24 minutes                                                            vigilant_austin
4b85c6f74e93   victorgame/ubuntu   "/bin/bash"              26 minutes ago      Exited (0) 26 minutes ago                                                trusting_driscoll
16ce50bd66ed   mysql               "docker-entrypoint.s…"   28 minutes ago      Exited (1) 28 minutes ago                                                festive_hugle
2ff5db049925   ubuntu              "/bin/bash"              43 minutes ago      Up 43 minutes                                                            zen_lamarr
dee9183f59c9   fernando93d/hello   "python ./app.py"        About an hour ago   Exited (0) About an hour ago                                             optimistic_khayyam
55878aa26b36   nginx               "/docker-entrypoint.…"   2 hours ago         Up 2 hours                     0.0.0.0:49153->80/tcp, :::49153->80/tcp   admiring_golick
29e1a472c8cc   nginx               "/docker-entrypoint.…"   2 hours ago         Up 2 hours                     0.0.0.0:8080->80/tcp, :::8080->80/tcp     focused_babbage
90f41e81e526   nginx               "/docker-entrypoint.…"   2 hours ago         Up 2 hours                     0.0.0.0:80->80/tcp, :::80->80/tcp         wizardly_neumann

# eliminar el contenedor
➜  docker git:(master) ✗ docker container rm c4ce0941a3f4
Error response from daemon: You cannot remove a running container c4ce0941a3f40617b7b2ed90712867d682039ce16f7c2a0d1db562d733558c9d. Stop the container before attempting removal or force remove

# removemos el contenedor con -f
➜  docker git:(master) ✗ docker container rm -f c4ce0941a3f4
c4ce0941a3f4
➜  docker git:(master) ✗

# Inspeccionamos el volumen 
➜  docker git:(master) ✗ sudo ls /var/lib/docker/volumes/local/_data
a  b  c
➜  docker git:(master) ✗

# Corremos un nuevo contenedor
➜  docker git:(master) ✗ docker container run -it -v local:/src victorgame/ubuntu
root@78663f147348:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  src  srv  sys  tmp  usr  var
root@78663f147348:/# cd src
root@78663f147348:/src# ls
a  b  c
root@78663f147348:/src#

# Persistencia de datos, al eliminar el contenedor.
```

## Compartiendo archivos con contenedores

```bash
# archivos | en el directorio app
  docker git:(master) ✗ docker container run -it -v local:/app victorgame/ubuntu
root@c625053d01db:/# cd app
root@c625053d01db:/app# ls
a  b  c
root@c625053d01db:/app# ls
a
root@c625053d01db:/app#

# Remover directorio desde src
➜  ~ docker container run -it -v local:/src victorgame/ubuntu
root@474c0795f193:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  src  srv  sys  tmp  usr  var
root@474c0795f193:/# cd src
root@474c0795f193:/src# ls
a  b  c
root@474c0795f193:/src# rm b c
root@474c0795f193:/src#

# Comparitiendo archivos de del directorio src de equipo a app en docker
➜  docker git:(master) ✗ docker container run -it -v /home/chronos/Documents/Learning_codigofacilito/docker/src:/app victorgame/ubuntu
root@19ff071e32c3:/# ls
app  bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@19ff071e32c3:/# cd app
root@19ff071e32c3:/app# ls
index.html
root@19ff071e32c3:/app# ls
index.html  index.js
root@19ff071e32c3:/app#

# directoio
➜  ~ touch /home/chronos/Documents/Learning_codigofacilito/docker/src/index.js

# Compartir un archivo en especifico
➜  ~ docker container run -d -v /home/chronos/Documents/Learning_codigofacilito/docker/src/index.html:/usr/share/nginx/html/index.html -p 80:80 nginx
b46dd63a28c555306f35f2768a613d1770c0e5d21732b01296f8dd60b6a868f4
➜  ~ curl localhost
<h1>Hola</h1>
<h2>Curso de docker</h2>
➜  ~

```

# 4. Imagenes

##  Overview Imágenes

```bash
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY datos.txt /app

CMD ["echo", "Hola"]
```

## Dockerfile

```bash
# crear Dockerfile
➜  docker git:(master) ✗ nano Dockerfile

# Ejecutamos el docker file
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu .
Sending build context to Docker daemon  22.02kB
Step 1/3 : FROM victorgame/ubuntu                     # crea el contenedores
 ---> 7e0aa2d69a15
Step 2/3 : RUN mkdir /app                             # Crea el directorio app
 ---> Running in 674ef8aed12e
Removing intermediate container 674ef8aed12e
 ---> 1ff03ca4b5a5
Step 3/3 : RUN cd /app && touch data.txt              # Se mueve al directorio app y crea el archivo data.txt
 ---> Running in 2a8d9cc6988d
Removing intermediate container 2a8d9cc6988d
 ---> 8ab3b6c9cdea
Successfully built 8ab3b6c9cdea                       # Proceso finalizado
Successfully tagged victorgame/ubuntu:latest
➜  docker git:(master) ✗

# listamos los contenedores
➜  docker git:(master) ✗ docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
victorgame/ubuntu   latest    8ab3b6c9cdea   2 minutes ago   72.7MB
ubuntu-file         latest    38d09fc700fd   2 hours ago     72.7MB
ubunut-file         latest    fd20544d545b   3 hours ago     72.7MB
ubuntu              latest    7e0aa2d69a15   9 days ago      72.7MB
victorgame/ubuntu   <none>    7e0aa2d69a15   9 days ago      72.7MB
mysql               latest    0627ec6901db   13 days ago     556MB
nginx               latest    62d49f9bab67   2 weeks ago     133MB
fernando93d/hello   latest    7fe934464560   2 years ago     150MB

# Corremos un nuevo contenedor
➜  ~ docker container run -it victorgame/ubuntu
root@e4c337e93360:/# ls
app  bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@e4c337e93360:/# cd app

# Vemos el archivo data en el directorio app
root@e4c337e93360:/app# ls
data.txt
root@e4c337e93360:/app#
```

## Copiar archivos

```bash
# Crear la imagen
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v2 .
Sending build context to Docker daemon  23.04kB
Step 1/4 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/4 : RUN mkdir /devops
 ---> Running in e82293499704
Removing intermediate container e82293499704
 ---> 4f9f658ff8cc
Step 3/4 : RUN cd /devops && touch data.txt
 ---> Running in 499769c907a6
Removing intermediate container 499769c907a6
 ---> e829f539bfd4
Step 4/4 : COPY ./src/data /app/src/com/data.txt
 ---> dab5a4b8be72
Successfully built dab5a4b8be72
Successfully tagged victorgame/ubuntu:v2
➜  docker git:(master) ✗

# Copiar archivos satisfactoriamente
➜  docker git:(master) ✗ nano Dockerfile
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubuntu:v2
root@2e7c25f02f3b:/# cd app/
root@2e7c25f02f3b:/app# ls
data.txt  src
root@2e7c25f02f3b:/app# cat data.txt
root@2e7c25f02f3b:/app# cd src/
root@2e7c25f02f3b:/app/src# ls
com
root@2e7c25f02f3b:/app/src# cd com/
root@2e7c25f02f3b:/app/src/com# ls
data.txt
root@2e7c25f02f3b:/app/src/com# cat data.txt
Hola

Bienvenido al curso de docker

Sois geniales chicos!!!!!
root@2e7c25f02f3b:/app/src/com#
```

El docker container se desctruye despues de salir agregando --agregamos

```bash
# contruimos image
➜  docker git:(master) ✗ docker image build -t victorgame/ubutu:v3 .
Sending build context to Docker daemon  23.04kB
Step 1/4 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/4 : RUN mkdir /devops
 ---> Using cache
 ---> 4f9f658ff8cc
Step 3/4 : RUN cd /devops && touch data.txt
 ---> Using cache
 ---> e829f539bfd4
Step 4/4 : COPY ./src /app/src
 ---> 2e9cee6809ea
Successfully built 2e9cee6809ea
Successfully tagged victorgame/ubutu:v3

# comprobamos que los archivos se han copiado
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubutu:v3
root@aacd42c3428b:/# cd app/
root@aacd42c3428b:/app# cd src/
root@aacd42c3428b:/app/src# ls
data  index.html  index.js
root@aacd42c3428b:/app/src#

# Contenedor destruido
➜  docker git:(master) ✗ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
➜  docker git:(master) ✗
```

ADD en Dockerfile

```bash
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v4 .
Sending build context to Docker daemon  28.67kB
Step 1/6 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/6 : RUN mkdir /devOps
 ---> Using cache
 ---> b7e8f1dd3a14
Step 3/6 : RUN cd /devOps && touch data.txt
 ---> Using cache
 ---> b0de85899634
Step 4/6 : COPY ./src/data /app/src/com/data.txt
 ---> Using cache
 ---> 6877f0e1f8cf
Step 5/6 : COPY ./src /app/src
 ---> Using cache
 ---> 3aa50928e9e4
Step 6/6 : ADD archivos.tar.gz /com/src
 ---> 5a8b515649cd
Successfully built 5a8b515649cd
Successfully tagged victorgame/ubuntu:v4
➜  docker git:(master) ✗

# Archivos agregados
root@e99033b7393c:/# ls
app  bin  boot  com  dev  devOps  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@e99033b7393c:/#
```

## Variables de entorno

env, agrendando -e al comando

```bash
➜  docker git:(master) ✗ docker container run -it --rm -e USER=$USER victorgame/ubuntu
root@e668fc365afc:/# echo $USER
chronos
root@e668fc365afc:/#

# Crear variable de entorno Codi
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v5 .
Sending build context to Docker daemon  28.67kB
Step 1/7 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/7 : ENV USER Codi
 ---> Running in b3ab2faad839
Removing intermediate container b3ab2faad839
 ---> 515367a9e1da
Step 3/7 : RUN mkdir /devOps
 ---> Running in 0ef3ee5d8cf3
Removing intermediate container 0ef3ee5d8cf3
 ---> 6f133a6445db
Step 4/7 : RUN cd /devOps && touch data.txt
 ---> Running in 26e9ba8f2fad
Removing intermediate container 26e9ba8f2fad
 ---> aa87fe6cc8dc
Step 5/7 : COPY ./src/data /app/src/com/data.txt
 ---> 22e8e89eb1ec
Step 6/7 : COPY ./src /app/src
 ---> e7812e9fc678
Step 7/7 : ADD archivos.tar.gz /com/src
 ---> b65cf0f79d4f
Successfully built b65cf0f79d4f
Successfully tagged victorgame/ubuntu:v5
➜  docker git:(master) ✗

# variable de entorno
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubuntu:v5
root@b53c7ebdfd83:/# echo $USER
Codi
root@b53c7ebdfd83:/#

# Remplazando usuario
➜  docker git:(master) ✗ docker container run --rm -it  -e USER="Victor" victorgame/ubuntu:v5
root@d8851974e87d:/# echo $USER
Victor
root@d8851974e87d:/#
```

## Argumentos

ARG remplazables al momento de crear la imagen

```bash
# Dockerfile

ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

ENV USER Codi

RUN mkdir /devOps
RUN cd /devOps && touch data.txt

COPY ./src/data /app/src/com/data.txt

COPY ./src /app/src
ADD archivos.tar.gz /com/src

# Creamos la imagen
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v6 .
Sending build context to Docker daemon  28.67kB
Step 1/8 : ARG DISTRO="ubuntu:18.04"
Step 2/8 : FROM ${DISTRO}
18.04: Pulling from library/ubuntu
01bf7da0a88c: Pull complete
f3b4a5f15c7a: Pull complete
57ffbe87baa1: Pull complete
Digest: sha256:538529c9d229fb55f50e6746b119e899775205d62c0fc1b7e679b30d02ecb6e8
Status: Downloaded newer image for ubuntu:18.04
 ---> 4eb8f7c43909
Step 3/8 : ENV USER Codi
 ---> Running in ec6bee2ab524
Removing intermediate container ec6bee2ab524
 ---> 2e5451d7ceef
Step 4/8 : RUN mkdir /devOps
 ---> Running in b9854eda6696
Removing intermediate container b9854eda6696
 ---> 5c13aa524a5e
Step 5/8 : RUN cd /devOps && touch data.txt
 ---> Running in bc7f6456d824
Removing intermediate container bc7f6456d824
 ---> 37e9e2f2bae3
Step 6/8 : COPY ./src/data /app/src/com/data.txt
 ---> 7c65156275c2
Step 7/8 : COPY ./src /app/src
 ---> 86b2e2b496d7
Step 8/8 : ADD archivos.tar.gz /com/src
 ---> f87f8bb9b8ac
Successfully built f87f8bb9b8ac
Successfully tagged victorgame/ubuntu:v6
➜  docker git:(master) ✗

# Cambiar de Distro al crear el contenedor
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v6 --build-arg DISTRO=ubuntu:19.04 .
Sending build context to Docker daemon  28.67kB
Step 1/8 : ARG DISTRO="ubuntu:18.04"
Step 2/8 : FROM ${DISTRO}
19.04: Pulling from library/ubuntu
4dc9c2fff018: Pull complete
0a4ccbb24215: Pull complete
c0f243bc6706: Pull complete
5ff1eaecba77: Pull complete
Digest: sha256:2adeae829bf27a3399a0e7db8ae38d5adb89bcaf1bbef378240bc0e6724e8344
Status: Downloaded newer image for ubuntu:19.04     # Cambio de distro
 ---> c88ac1f841b7
Step 3/8 : ENV USER Codi
 ---> Running in 64b14261e598
Removing intermediate container 64b14261e598
 ---> bd15b0d19488
Step 4/8 : RUN mkdir /devOps
 ---> Running in c09f0c3a7258
Removing intermediate container c09f0c3a7258
 ---> bb458fd8298e
Step 5/8 : RUN cd /devOps && touch data.txt
 ---> Running in ef37cbd1130c
Removing intermediate container ef37cbd1130c
 ---> 33f6cf4318c6
Step 6/8 : COPY ./src/data /app/src/com/data.txt
 ---> ed247c39ae6c
Step 7/8 : COPY ./src /app/src
 ---> fa64d9b8fec7
Step 8/8 : ADD archivos.tar.gz /com/src
 ---> acfe73a6f0a8
Successfully built acfe73a6f0a8
Successfully tagged victorgame/ubuntu:v6
➜  docker git:(master) ✗
```


## Dockerignore

```bash
# Creamos la imagen del contenedor
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v8 .
Sending build context to Docker daemon  33.79kB
Step 1/5 : ARG DISTRO="ubuntu:18.04"
Step 2/5 : FROM ${DISTRO}
 ---> 4eb8f7c43909
Step 3/5 : RUN mkdir devOps
 ---> Running in 621d24863239
Removing intermediate container 621d24863239
 ---> d85cb3971a04
Step 4/5 : RUN cd /devOps && touch data.txt
 ---> Running in 6f6ca0f35111
Removing intermediate container 6f6ca0f35111
 ---> a992ddc66c7d
Step 5/5 : COPY ./src /devOps/src
 ---> be574f099eae
Successfully built be574f099eae
Successfully tagged victorgame/ubuntu:v8
➜  docker git:(master) ✗

# archivo agregado ls
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubuntu:v8
root@dc3b2783ff08:/# ls
bin  boot  dev  devOps  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@dc3b2783ff08:/# cd devOps/
root@dc3b2783ff08:/devOps# ls
data.txt  src
root@dc3b2783ff08:/devOps# cd src/
root@dc3b2783ff08:/devOps/src# ls
data  index.html  index.js  ls
root@dc3b2783ff08:/devOps/src#
```

Crear el archivo `.dockerignore` en la misma ruta que el `Dockerfile`.

```bash
# .dockerignore
./src/html
./src/ls
./src/*.conf


# Crear la imagen 
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v9 .
Sending build context to Docker daemon  35.33kB
Step 1/5 : ARG DISTRO="ubuntu:18.04"
Step 2/5 : FROM ${DISTRO}
 ---> 4eb8f7c43909
Step 3/5 : RUN mkdir devOps
 ---> Using cache
 ---> d85cb3971a04
Step 4/5 : RUN cd /devOps && touch data.txt
 ---> Using cache
 ---> a992ddc66c7d
Step 5/5 : COPY ./src /devOps/src
 ---> 07e6613d20ad
Successfully built 07e6613d20ad
Successfully tagged victorgame/ubuntu:v9
➜  docker git:(master) ✗


# corremos el contenedor
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubuntu:v9
root@71302ebfeca6:/# ls
bin  boot  dev  devOps  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@71302ebfeca6:/# cd devOps/
root@71302ebfeca6:/devOps# ls
data.txt  src
root@71302ebfeca6:/devOps# cd src/
root@71302ebfeca6:/devOps/src# ls
data  index.html  index.js
root@71302ebfeca6:/devOps/src#
```

## Trabajando con usuarios

Siempre trabajamos con el usuario root

```bash
# Creamos la imagen con el usuario
➜  docker git:(master) ✗ docker image build -t victorgame/ubuntu:v10 .
Sending build context to Docker daemon  35.33kB
Step 1/8 : ARG DISTRO="ubuntu:18.04"
Step 2/8 : FROM ${DISTRO}
 ---> 4eb8f7c43909
Step 3/8 : RUN useradd -ms /bin/bash cloud_user
 ---> Running in 605453071eb7
Removing intermediate container 605453071eb7
 ---> e613c180538b
Step 4/8 : RUN mkdir devOps
 ---> Running in e2ea41d13c2f
Removing intermediate container e2ea41d13c2f
 ---> 44def5dc3d14
Step 5/8 : RUN cd /devOps && touch data.txt
 ---> Running in ff51f33112cb
Removing intermediate container ff51f33112cb
 ---> 5e72421b9425
Step 6/8 : COPY ./src /devOps/src
 ---> 83edc452fb57
Step 7/8 : USER cloud_user
 ---> Running in 603abcf4b589
Removing intermediate container 603abcf4b589
 ---> 8f2a14957251
Step 8/8 : RUN cd /home/cloud_user && touch data.txt
 ---> Running in f80615bdaa92
Removing intermediate container f80615bdaa92
 ---> 49690a641044
Successfully built 49690a641044
Successfully tagged victorgame/ubuntu:v10
➜  docker git:(master) ✗

# Corremos el contenedor
➜  docker git:(master) ✗ docker container run --rm -it victorgame/ubuntu:v10
cloud_user@ca8f74a86508:/$ ls
bin  boot  dev  devOps  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
cloud_user@ca8f74a86508:/$ ls home/
cloud_user
cloud_user@ca8f74a86508:/$ ls home/cloud_user/
data.txt
cloud_user@ca8f74a86508:/$

# ingresando como root
➜  docker git:(master) ✗ docker container exec -u 0 -it 44317365a0ad  bash
root@44317365a0ad:/# ls
bin  boot  dev  devOps  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@44317365a0ad:/# cd usr
root@44317365a0ad:/usr# ls
bin  games  include  lib  local  sbin  share  src
root@44317365a0ad:/usr# cd games/
root@44317365a0ad:/usr/games# ls
root@44317365a0ad:/usr/games# cd ..
root@44317365a0ad:/usr# ls
bin  games  include  lib  local  sbin  share  src
root@44317365a0ad:/usr# cd ..
root@44317365a0ad:/# ls
bin  boot  dev  devOps  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@44317365a0ad:/#
```

## Ejecutando comandos CMD

Ejecutar un script o comando con CMD

```bash
# Creamos contenedor CMD
➜  docker git:(master) ✗ docker image build -t cmd .
Sending build context to Docker daemon  40.96kB
Step 1/2 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/2 : CMD ["echo", "Hola mundo", "Desde Docker"]
 ---> Running in 39358285563b
Removing intermediate container 39358285563b
 ---> c1ff5b9480cd
Successfully built c1ff5b9480cd
Successfully tagged cmd:latest
➜  docker git:(master) ✗

# Ejecutamos el contenedor con cmd
➜  docker git:(master) ✗ docker container run cmd
Hola mundo Desde Docker
➜  docker git:(master) ✗
```

## CMD VS ENTRYPOINT

Ejecutar el cmd no es la mejor manera de ejecutar comandos o escripts. Lo solucionamos con el 
entrypoint.

Lo que declaramos en el cmd es remplazable...

Entrypoint no es remplazada

```bash
➜  docker git:(master) ✗ docker container run cmd
Hola mundo Desde Docker

# Cambiar mensaje
➜  docker git:(master) ✗ docker container run cmd echo "Codi"
Codi
➜  docker git:(master) ✗

# Contenedor  ENTRYPOINT
➜  docker git:(master) ✗ docker image build -t cmd2 .
Sending build context to Docker daemon  40.96kB
Step 1/2 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/2 : ENTRYPOINT ["echo", "Hola, Mundo"]
 ---> Running in ae990cd90907
Removing intermediate container ae990cd90907
 ---> d3868def852e
Successfully built d3868def852e
Successfully tagged cmd2:latest
➜  docker git:(master) ✗

# Dockerfile
FROM victorgame/ubuntu          # Es una copia de ubuntu 

ENTRYPOINT ["echo", "Hola, Mundo"]

# Contenedor 
➜  docker git:(master) ✗ docker container run cmd2
Hola, Mundo
➜  docker git:(master) ✗ docker container run cmd2 echo "Codi"
Hola, Mundo echo Codi
➜  docker git:(master) ✗

# CMD & ENTRYPOINT
➜  docker git:(master) ✗ docker image build -t cmd3 .
Sending build context to Docker daemon  40.96kB
Step 1/3 : FROM victorgame/ubuntu
 ---> 8ab3b6c9cdea
Step 2/3 : ENTRYPOINT ["echo"]
 ---> Running in 40bf63658f05
Removing intermediate container 40bf63658f05
 ---> 745f8aa30fd3
Step 3/3 : CMD [ "Hola"]
 ---> Running in 3674e401aa8a
Removing intermediate container 3674e401aa8a
 ---> 278527189b23
Successfully built 278527189b23
Successfully tagged cmd3:latest
➜  docker git:(master) ✗ docker container run cmd3
Hola
➜  docker git:(master) ✗
```

CMD datos remplazables

ENTRYPOINT no remplazables, la informacion nueva se agrega a la cadena de texto.

## Contenerizar app

Creamos el archivos [index.js](app/index.js)

Descargar el contenedor de node

```bash
docker pull node
```

Correr el contenedor 

- `/app` carpeta dentro del contenedor
- `../app` ubicacion del proyecto local
- `-w`
- `--rm` mata al contenedor al salir
- `/app:/app` nos ubica dentro del proyecto en el contenedor
- `-v`
- `node` contenedor

```bash
docker run --rm -w /app -v /home/chronos/Learning_codigofacilito/app:/app -it node

# Iniciamos nodejs ejecutamos mpn 
➜  docker git:(master) ✗ docker run --rm -w /app -v ~/Documents/Learning_codigofacilito/docker/app:/app -it node npm init -y
Wrote to /app/package.json:

{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}


npm notice
npm notice New minor version of npm available! 7.10.0 -> 7.11.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v7.11.2
npm notice Run npm install -g npm@7.11.2 to update!
npm notice

# Instlamos express 
➜  docker git:(master) ✗ docker run --rm -w /app -v ~/Documents/Learning_codigofacilito/docker/app:/app -it node npm install -S express

added 50 packages, and audited 51 packages in 39s

found 0 vulnerabilities
npm notice
npm notice New minor version of npm available! 7.10.0 -> 7.11.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v7.11.2
npm notice Run npm install -g npm@7.11.2 to update!
npm notice
➜  docker git:(master) ✗

# Eliminamos la caperpeta de node_modules
➜  docker git:(master) ✗ ls app
index.js  node_modules	package.json  package-lock.json
➜  docker git:(master) ✗ sudo rm -r app/node_modules

# Creamos el archivo de Docerfile
ROM node
WORKDIR /app
COPY package.json .
RUN npm install
COPY index.js .
CMD ["node", "index.js"]

# Creamos la imagen 
  app git:(master) ✗ docker image build -t web .
Sending build context to Docker daemon  36.35kB
Step 1/6 : FROM node
 ---> 6817534de6bd
Step 2/6 : WORKDIR /app
 ---> Using cache
 ---> 092ebcf82bb1
Step 3/6 : COPY package.json .
 ---> Using cache
 ---> e128246c4de8
Step 4/6 : RUN npm install
 ---> Running in 4151f063b95f

added 50 packages, and audited 51 packages in 52s

found 0 vulnerabilities
npm notice
npm notice New minor version of npm available! 7.10.0 -> 7.11.2
npm notice Changelog: <https://github.com/npm/cli/releases/tag/v7.11.2>
npm notice Run `npm install -g npm@7.11.2` to update!
npm notice
Removing intermediate container 4151f063b95f
 ---> 906ac0893cc9
Step 5/6 : COPY index.js .
 ---> 48315f01de01
Step 6/6 : CMD ["node", "index.js"]
 ---> Running in 277e80f95860
Removing intermediate container 277e80f95860
 ---> 5eabd838edda
Successfully built 5eabd838edda
Successfully tagged web:latest
➜  app git:(master) ✗

# Ejecutamos el contendedor
➜  app git:(master) ✗ docker run -d -p 3000:3000 web
b9248e21a2e3b883b8f70b85f1aea8b158498f88d1a7a9d101c63ef6b2d1deb4
➜  app git:(master) ✗ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                       NAMES
b9248e21a2e3   web       "docker-entrypoint.s…"   6 seconds ago   Up 4 seconds   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   loving_khorana
➜  app git:(master) ✗

➜  app git:(master) ✗ curl localhost:3000
Hola mundo%                                                                                                                                  
➜  app git:(master) ✗
```

## Subir imagen al docker hub

- [Docker Hub]()

Creamos una cuenta

En terminal nos logeamos con 

```bash
docker login
```

Ingresamos las credenciasles


Para subir un contemedor a docker hub 
-- 

Utilizamos el comando `docker pull`

```bash
# listamos los contenedores 
➜  app git:(master) ✗ docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
web                 latest    5eabd838edda   7 minutes ago   912MB    # Nuestro contenedor
cmd3                latest    278527189b23   2 hours ago     72.7MB
cmd2                latest    d3868def852e   2 hours ago     72.7MB
cmd                 latest    c1ff5b9480cd   2 hours ago     72.7MB
victorgame/ubuntu   v10       49690a641044   3 hours ago     63.5MB
victorgame/ubuntu   v9        07e6613d20ad   3 hours ago     63.1MB
victorgame/ubuntu   v8        be574f099eae   4 hours ago     63.1MB
victorgame/ubuntu   v6        acfe73a6f0a8   4 hours ago     70MB
<none>              <none>    f87f8bb9b8ac   4 hours ago     63.1MB
victorgame/ubuntu   v5        b65cf0f79d4f   4 hours ago     72.7MB
victorgame/ubuntu   v4        5a8b515649cd   4 hours ago     72.7MB
victorgame/ubutu    v3        2e9cee6809ea   13 hours ago    72.7MB
victorgame/ubuntu   v2        dab5a4b8be72   13 hours ago    72.7MB
victorgame/ubuntu   latest    8ab3b6c9cdea   13 hours ago    72.7MB
ubuntu-file         latest    38d09fc700fd   16 hours ago    72.7MB
ubunut-file         latest    fd20544d545b   16 hours ago    72.7MB
node                latest    6817534de6bd   6 days ago      907MB
ubuntu              latest    7e0aa2d69a15   9 days ago      72.7MB
victorgame/ubuntu   <none>    7e0aa2d69a15   9 days ago      72.7MB
ubuntu              18.04     4eb8f7c43909   9 days ago      63.1MB
mysql               latest    0627ec6901db   13 days ago     556MB
nginx               latest    62d49f9bab67   2 weeks ago     133MB
ubuntu              19.04     c88ac1f841b7   15 months ago   70MB
fernando93d/hello   latest    7fe934464560   2 years ago     150MB
➜  app git:(master) ✗

# Subinos nuestro contendore a docker Hub Y renombramos al contendor
➜  app git:(master) ✗ docker tag web victorgame/node_app
➜  app git:(master) ✗ docer image ls
zsh: command not found: docer
➜  app git:(master) ✗ docker image ls
REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
victorgame/node_app   latest    5eabd838edda   10 minutes ago   912MB # nuestro contendor

➜  app git:(master) ✗ docker push victorgame/node_app
```

# 5. Redes

## Redes en Docker


## Inspeccionado redes

Inspeccionado la red 

```bash
➜  app git:(master) ✗ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "8f93fa3d9c0f2de503be5777473ebc6b76c43d35dffe4123ef603d8b321e5253",
        "Created": "2021-05-03T06:47:37.541666177-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
➜  app git:(master) ✗

# Corremos el contenedor ubunto 
  app git:(master) ✗ docker container run -dit victorgame/ubuntu
436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d
➜  app git:(master) ✗ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "8f93fa3d9c0f2de503be5777473ebc6b76c43d35dffe4123ef603d8b321e5253",
        "Created": "2021-05-03T06:47:37.541666177-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d": {
                "Name": "hopeful_galileo",
                "EndpointID": "b95db3ded0149a9058305018753a5b9c118b8481cb67f7850994ebe762112b01",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",  # ip agregada
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
➜  app git:(master) ✗
```

Inseccionamos el contenedor

```bash
➜  app git:(master) ✗ docker container inspect 436ce46b9119
[
    {
        "Id": "436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d",
        "Created": "2021-05-03T17:37:27.0287334Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 13237,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-05-03T17:37:28.378534779Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:8ab3b6c9cdea037b60b02b6c4c8879327f053c0a97962e98b083cc29409852dc",
        "ResolvConfPath": "/var/lib/docker/containers/436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d/hostname",
        "HostsPath": "/var/lib/docker/containers/436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d/hosts",
        "LogPath": "/var/lib/docker/containers/436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d/436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d-json.log",
        "Name": "/hopeful_galileo",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/147141a974e8345c240f330067f15eb8e4f61be084da2eb25495017105d77f2f-init/diff:/var/lib/docker/overlay2/2385458709c57bb918565a714d3e49bb6416411642e882e8102e7e173b1338ed/diff:/var/lib/docker/overlay2/c49fa57c595892d170a87acddb0b7f09b2e2e697f780c60b13484f34cfb2b026/diff:/var/lib/docker/overlay2/c060aebb4db5fd518265c7c0fdbe5f1d3e83dbb1876e03bf88efa5d4f9ccb436/diff:/var/lib/docker/overlay2/70e34051a738bbf205082b05c8604075fbcf48a2e6fb4bff52ffc705e556a976/diff:/var/lib/docker/overlay2/88c48510dfb9316e3e0675ddf842dff8162a4a9833e9d015899bff08f5b9848b/diff",
                "MergedDir": "/var/lib/docker/overlay2/147141a974e8345c240f330067f15eb8e4f61be084da2eb25495017105d77f2f/merged",
                "UpperDir": "/var/lib/docker/overlay2/147141a974e8345c240f330067f15eb8e4f61be084da2eb25495017105d77f2f/diff",
                "WorkDir": "/var/lib/docker/overlay2/147141a974e8345c240f330067f15eb8e4f61be084da2eb25495017105d77f2f/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "436ce46b9119",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "victorgame/ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "af80041ec9ffc6aaa9f8855c3f87aa962fe72e0ee9178fdfaf4831c9fef3084f",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/af80041ec9ff",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "b95db3ded0149a9058305018753a5b9c118b8481cb67f7850994ebe762112b01",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",   # ip
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "8f93fa3d9c0f2de503be5777473ebc6b76c43d35dffe4123ef603d8b321e5253",
                    "EndpointID": "b95db3ded0149a9058305018753a5b9c118b8481cb67f7850994ebe762112b01",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
➜  app git:(master) ✗
```

Conectar y Desconectar un contenedor

```bash
# Desconectar
➜  ~ docker container ls
CONTAINER ID   IMAGE               COMMAND       CREATED              STATUS              PORTS     NAMES
6392f32a2591   victorgame/ubuntu   "/bin/bash"   About a minute ago   Up About a minute             focused_tu
436ce46b9119   victorgame/ubuntu   "/bin/bash"   6 minutes ago        Up 6 minutes                  hopeful_galileo
➜  ~

➜  app git:(master) ✗ docker network disconnect bridge 436ce46b9119
➜  app git:(master) ✗

# connectar un contenerdor
➜  app git:(master) ✗ docker network connect bridge 436ce46b9119
➜  app git:(master) ✗ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "8f93fa3d9c0f2de503be5777473ebc6b76c43d35dffe4123ef603d8b321e5253",
        "Created": "2021-05-03T06:47:37.541666177-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "436ce46b911978a5ded0c5de52231f2ee4ea79431e794ce39725f6717379ec9d": {
                "Name": "hopeful_galileo",
                "EndpointID": "4e823e7c6fc6390d4b1774fcf6f5c850f33a13a4a52336f1ef185a281029c98c",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            },
            "6392f32a259107eb0eb5a38731d803c08178ac7655da371197e60a9476964f99": {
                "Name": "focused_tu",
                "EndpointID": "e4cb48550a55c205f59676d167bed386081b3e23d25b623a09a65aca1077e429",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
➜  app git:(master) ✗

# Detener los contenedores
➜  app git:(master) ✗ docker stop $(docker ps -q)
6392f32a2591
436ce46b9119
➜  app git:(master) ✗

# Eliminamos los contenedores
➜  app git:(master) ✗ docker container prune
```

```bash
➜  app git:(master) ✗ docker run -dit --network host ubuntu
7ec45c6480cff004620af4624c7bcc3f9360d1da67e73ce9d8053c448667cece

➜  app git:(master) ✗ docker network inspect host
[
    {
        "Name": "host",
        "Id": "8fa97ea33e1eab2fd7572ca00a37623fa27594b380aaeed8f82d1e92dd6d83d9",
        "Created": "2021-04-28T22:42:13.577849126-06:00",
        "Scope": "local",
        "Driver": "host",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": []
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "7ec45c6480cff004620af4624c7bcc3f9360d1da67e73ce9d8053c448667cece": {
                "Name": "intelligent_elgamal",
                "EndpointID": "baedd14ff7c5c546c8ff503dc7c7857b0a99a2a14d10901b8246bc3dd13b123d",
                "MacAddress": "",
                "IPv4Address": "",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
➜  app git:(master) ✗ docker container exec -it intelligent_elgamal bash

```

## Creando redes

Crear una red breach y genera una red.

Creamos nuestro archivo [Dockerfile](net/Dockerfile)

```bash
# en la carpeta net
➜  net git:(master) ✗ docker image build -t ubuntu-tools .

# Crear la red
docker network create br0

➜  net git:(master) ✗ docker network create br0
9307144e39e1ce875d23f7103eeb83730a05fdb3516f11ea881230c1618c71d3
➜  net git:(master) ✗ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
9307144e39e1   br0       bridge    local
8f93fa3d9c0f   bridge    bridge    local
8fa97ea33e1e   host      host      local
d4b8311d14f8   none      null      local
➜  net git:(master) ✗
```

Crear contenedores

```bash
 net git:(master) ✗ docker container run -dit --network br0 --name host1 ubuntu-tools bash
➜  net git:(master) ✗ docker container run -dit --network br0 --name host2 ubuntu-tools bash

➜  net git:(master) ✗ docker container ls
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS          PORTS     NAMES
4950019b9891   ubuntu-tools   "/bin/bash"   36 seconds ago   Up 33 seconds             host2
184d6c86a46c   ubuntu-tools   "/bin/bash"   49 seconds ago   Up 45 seconds             host1

# Contenedores con su propia ip
➜  net git:(master) ✗ docker container exec -it host4 bash
➜  net git:(master) ✗ docker container exec -it host5 bash

ping host4
ping host5
```

## Agregando Ip estática a contenedor

Crear un contenedor con una ip estatica

```bash
docker network create --subnet 10.1.0.0/24 --gateway 10.1.0.1 br02

# Listar redes
➜  net git:(master) ✗ docker network ls

# Inspeccionamos br02
➜  net git:(master) ✗ docker network inspect br02

# Contenedor con ip estatica
docker container run -it --ip 10.1.0.10 --network br02 ubuntu-tools

# El contenedor activo Inspeccionamos la red
docker network inspect br02
```

# 6. Docker Machine

## Overview docker machine

- [Install Docker Machine](https://docs.docker.com/machine/install-machine/)

## Creando máquina digitalocean

- [DigitalOcean](https://cloud.digitalocean.com/)
 
Conectar docker machine atreves del token de digitalocean

```bash
dicker-machine create -d digitalocean --digitalocean-access-token=<ingresar-token> local 

docker-machine ls
```

## Accediendo al docker machine

Comandos 

```bash
# virtual
docker-machine env local

docker machine ls

eval $(docker-machine env local)

docker image pull nginx


docker container run -d -p 80:80 nginx

# Obtener ip local
docker-machine ip local

# docker ssh
docker-machine ssh local

# Eliminar docker-machine
docker-machine rm local
```

# 7. Docker Compose

## Docker compose overview

Multiple contenedores

Docker-compose se establece con la extension `.yml`

- [file docker-compose](docker-compose.yml)

Corremos el contenedor:

```bash
docker-compose up

# Contenedor en segundo plano
➜  docker git:(master) ✗ docker-compose up -d
Starting docker_nginx_1 ... done
➜  docker git:(master) ✗
➜  docker git:(master) ✗ docker-compose ps
     Name                   Command               State                Ports
------------------------------------------------------------------------------------------
docker_nginx_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp,:::80->80/tcp

# destruir el contenedor
➜  docker git:(master) ✗ docker-compose down
Stopping docker_nginx_1 ... done
Removing docker_nginx_1 ... done
Removing network docker_default
➜  docker git:(master) ✗

```

- [Docker-compose](https://docs.docker.com/compose/install/)


## Servicios

```bash
# Integra mysql al docker-compose.yml
  docker git:(master) ✗ docker-compose ps
Name               Command               State                 Ports
----------------------------------------------------------------------------------
mysql   docker-entrypoint.sh mysqld      Exit 1


# El puert 3306 debe estar libre, de lo contrario tendriamos problemas
➜  docker git:(master) ✗ docker-compose ps
Name               Command               State                          Ports
----------------------------------------------------------------------------------------------------
mysql   docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp
nginx   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:80->80/tcp,:::80->80/tcp
➜  docker git:(master) ✗

```

## Variables de entorno

Crear el archivo .env, donde almacenaremos todo informacion sencible que no queremos subir a un repositorio o la publicar el proyecto

archivo [`.env`](.env)


## Redes

Configurar la red en el docker-compose.yml

```bash
networks:
  lorem:
    driver: bridge
```

Inspeccionamos la red

```bash
docker inpsect docker_lorem
```

Agregar el contenedor a una red existente

```bash
mysql:
  networks:
    - br0

networks:
  br0: # red existente
    extenal: true

# Inspeccionamos con
docker inpsect id
```

## Volúmenes

```docker
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html
    
    volumes:
      - mysql:/var/lib/mysql
      -
volumes:
  mysql:
```

Volvemos a ejecutar 

```bash
docker-compose up -d
```

Los archivos se cargan en los directorios.

# 8. Orquestadores

## Orquestadores teoría

Nodos
--

Swarm
--

Servicios
--

Tareas
--

## Docker swarm

Crear maquinas virutales en virtualbox

Instalar [Virtualbox | ArchLinux](https://geekytheory.com/como-instalar-virtualbox-en-arch-linux)

```bash
docker-machine create -d virtualbox manager1
docker-machine create -d virtualbox manager3
docker-machine create -d virtualbox manager2
```

```bash
docker-machine ls

# Iniciar un contenedor virtual
docker-machine ssh worker1

# Gnerar un token
docker swarm init --advertise-addr ip

# Tokens
docker swarm join --token SWMTKN-1-272rucub4s74wmtdddml9tdjhqfxjt067p6xxg5h07ul16vucg-8704l03q97eactvjdrdsee0ml 192.168.99.100:2376

# node
docker node ls

# ingrear a docker manager3-3
➜  docker git:(master) ✗ docker-machine ssh manager3-3
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

 # instalar redis
docker@manager3-3:~$ docker service create --replicas 1 --name redis redis:4

docker@manager3-3:~$ docker service ls
docker@manager3-3:~$ docker service inspect --pretty redis

# Eliminar un contenedor 
docker service rm 
```

- [Redin Skala](http://www.redinskala.com/2019/04/16/comandos-docker/)

## Docker swarm deploy servicio

```bash
docker service create --replicas 1 --name nginx nginx1
```



## Docker swarm actualizar puertos

Exponer puertos

```bash
docker service update --publish-add 80:80 nginx

# servicios de replicas
docker service update --replicas 3 nginx

# Activar docker-machine
docker-machine start <nombre>
```


## Kubernetes conceptos

Kubectl
--

Master Node
--

Worker Node
--

Kubelet
--

Kubernetes Pod
--

Deployment
--



## Kubernetes en local minikube

- [Kubernetes | minikube](https://github.com/kubernetes/minikube)

- [Instalar y Configurar kubectl](https://kubernetes.io/es/docs/tasks/tools/install-kubectl/) 

```bash
minikube start

# cli
kubectl

# nginx
kubectl run nginx --image=nginx

# kubectl
kubectl get pods

kubectl get deployments

```

# 9. Extras

## Compartiendo dispositivos con el contenedor

`--divese`
`moc` reproducir archivos mp4 en consola

```bash
➜  docker git:(master) ✗ docker run --rm -it -v /home/chronos/Documents/Learning_codigofacilito/docker:/home victorgame/ubuntu bash

apt-get install moc moc-ffmpeg-plugin

# --device
➜  docker git:(master) ✗ docker run --rm -it -v /home/chronos/Documents/Learning_codigofacilito/docker:/home --device /dev/snd  victorgame/ubuntu bash
```

Compartir y abrir aplicaciones graficas en un contenedor [jessfraz | dockerfiles](https://github.com/jessfraz/dockerfiles)

## Docker api

```bash
docker run -dit -v $PWD:/home/app -v /var/run/docker.sock:/var/run/docker.sock python:3.6

docker exec -it id bash
```

script [app.py](app.py)


## Proxy reversivo

configure 

- [docker-compose](proxi-reversivo/docker-compose.yml)
- [traefik.toml](proxi-reversivo/traefik.toml) 

```bash
docker-compose up -d

# labels
docker-compose up -d --force-recreate
```

- [traefiklabs](https://doc.traefik.io/traefik/)

