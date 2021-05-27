<h1>Nginx</h1>

<h3>Luis Fernando Garcia Perez</h3>

<h1>Tabla de Contenido</h1>


# 1. Introducción

## Presentación

Nginx?
Servidor web... funciona asincrona usando eventos, utilizando un solo evento.

- Nginx plus
- Nginx free

## Conceptos

Directivas

```nginx
http {
  directive "string"
}
```

Contexto

Core cibtexts

  - Mian
  - Events
  - https
  - Server 
  - Location
  - Upstream
  - Mail
  - If

## Instalación

``` BASH
# Instalar nginx
sudo pacman -S nginx
```

Ver status de nginx

``` BASH
#  status
sudo systemctl status nginx
```

``` BASH
# activar nginx
sudo systemctl start nginx
```

``` BASH
# Detener nginx
sudo systemctl stop nginx
```

activar nginx en el sistema
``` BASH
sudo systemctl enable nginx
```



# 2. Introducción a Nginx

## Configuración por default

``` BASH
cd /ect/nginx/
```


## VirtualHosts

- [Module nginx](https://nginx.org/en/docs/http/ngx_http_core_module.html)


``` BASH
# obtener ip
ifconfig
# o 
nmcli device show

# Editar archivo en
cd /etc/hosts
```

Configurar el archivo hostname, en arch hosts
``` BASH
# IP
ip app.test
ip apache.app.test
ip nginx.app.test
ip whoaim.app.test
```

Luego, modificar `localhost` por `app.test` en el directorio 
``` BASH
cd /etc/nginx/conf.f

# editar el archivo deaful.conf
: localhost => : app.test
# luego ir al navegador, escribir en la barara de nvegacion app.test


# Verificar que la configuracion y sitaxis este correcto con 
sudo nginx -t

# recargar nginx
sudo  nginx -s reload
```

## Default server

```bash
default_server
```


## Página de errores

```bash
error_page 404 = /404.html;
```

## Location

Instalar 
```bash
sudo apt-get install apache2-utils -y
```

Configuramos nuestro directorio en la ruta `/etc/nginx/conf.d`

```bash
sudo mkdir /etc/apache2
```
Configuramos nuestro registro admin

``` BASH
sudo htpasswd -c /etc/apache2/.htpasswd admin
# Ingresamos el password
```

Configuracion al archivo `default.conf`
```bash
location /admin {
  auth_basic "Admin";
  auth_basic_user_file "/etc/apache/.htpasswd";
}
```

# 3. Nginx como reverse proxy

## Qué es un proxy reversivo

Peticion atraves de un proxy.
Proxy reversivo el servidor hacer una peticion a un client.

## Proxy pass

Crear contenedores con Docker

``` BASH
# apache
docker run -dp 8080:80 http

# nginx
docker run -dp *808:80 nginx
```


``` BASH
# apach
location /apache {
  proxy_pass http://localhost:8080/;
}
location /nginx {
  proxy_pass http://localhost:8081/;
}
```


## Qué es fastCGI

FastCGI is a binary protocol for interfacing interactive programs with a web server. It is a bariation on the earlinercommon Gateway Interface (CGI)

Instalar `php-fpm`
``` BASH
sudo apt-get install php-fpm
```


## Configurando php con fastcgi_pass

proxy
``` BASH
# carpeta php
cd /run/php

# copiar la ruta
pwd
```

Nginx
``` BASH
# moverse al directorio conf.d
cd /etc/nginx/conf.d

# configuracion del archivo default.conf
root /usr/share/nginx/foo;
index index.html index.php;

location ~\.php$ {
  fastcgi_pass unix:/var/php/php8-fm.sock;
  fastcgi_index index.php;
  fastcgi_param SRIPT_FILENAME $realpath_root$fastcgi_script_name;
  include fastcgi_params;
}
```

``` BASH
# Moverser a nginx
cd ..
cd /etc/nginx

# Realizaar un catal archivo fastcgi_params
cat fastcgi_params
```

Crear nuevo archivo.html 
``` BASH
cd /usr/share/nginx/foo

# eliminar el archivo index.html
sudo rm index.html

# Crear nuevo archivo index.pp
sudo index.php
```

Contenido de `index.php`

```php
<?php
phpinfo();
```

Ver errores
```bash
sudo tail /var/log/nginx/error.log
```

# 4. Nginx como balanceador de cargas

## Qué es el balanceo de cargas

                               -> procesos
User -> Load Balancer ->       -> procesos
                              -> procesos
## Balanceo de cargas

Infraestructura de 4 servidores.

Ir al directorio `conf.d`
```bash
cd /etc/nginx/conf.d
```

configuracion upstream

```bash
upstream backend {
  server 172.24.7.252;
  server 172.24.7.77;
  server 172.24.0.4;
}

server {

  listen 80;

  location / {
    proxy_pass http://bakcken;
  }
}
```

## Examinando métodos de balanceo

configuracion upstream

```bash
upstream backend {
  round_robin;
  ip_hash;
  # server 172.24.7.252 wight=3;
  server 172.24.7.252 wight=3;
  server 172.24.7.77;
  server 172.24.0.4;
}

server {

  listen 80;
  
  location / {
    proxy_pass http://bakcken;
  }
}
```

- [Choosing an NGINX Plus Load‑Balancing Technique](https://www.nginx.com/blog/choosing-nginx-plus-load-balancing-techniques/)

# 5. Https

## Configurando certificado

Configuracion `default.conf`.

```bash
server {
  listen 80 default_server;
  # listen [::]:80 default_server;
  root /usr/share/nginx/html;
  server_name fernandol8s.com;

  listen 443 ssl;

  ssl_certificate /etc/letsenncrypt/live/fernandok8s.com/fullchain.pen;
  ssl_sertificate_key /etc/letsenncrypt/live/fernandok8s.com/privkey.pem;
  include /etc/letsencrypt/options-ssl-nginx.conf;

}
```

- [Crear certificado para nuestro dominio](https://www.youtube.com/watch?v=XD0JAx4G_7k)

## Redirección a https

Configuracion `default.conf`.

```bash
server {
  listen 80 default_server;
  # listen [::]:80 default_server;
  root /usr/share/nginx/html;
  server_name fernandol8s.com;

  listen 443 ssl;

  ssl_certificate /etc/letsenncrypt/live/fernandok8s.com/fullchain.pen;
  ssl_sertificate_key /etc/letsenncrypt/live/fernandok8s.com/privkey.pem;
  include /etc/letsencrypt/options-ssl-nginx.conf;

  if($scheme != "https") {
    return 301 https://$host$request_uri;
  }

}
```


