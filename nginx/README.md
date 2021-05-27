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

```html
a

# 3. Nginx como reverse proxy

## Qué es un proxy reversivo



## Proxy pass



## Qué es fastCGI



## Configurando php con fastcgi_pass



# 4. Nginx como balanceador de cargas

## Qué es el balanceo de cargas



## Balanceo de cargas



## Examinando métodos de balanceo



# 5. Https

## Configurando certificado



## Redirección a https




