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


## Variables de entorno
## Argumentos
## Dockerignore
## Trabajando con usuarios
## Ejecutando comandos CMD
## CMD VS ENTRYPOINT
## Contenerizar app
## Subir imagen al docker hub

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

