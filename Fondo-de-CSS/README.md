<h1>Fondo de CSS</h1>

<h3>Petriz Celaya</h3>

<h1>Tabla de Contenido</h1>

- [1. Introducción](#1-introducción)
  - [Introducción a CSS](#introducción-a-css)
  - [Selectores CSS](#selectores-css)
  - [Formas de integrar código CSS a nuestra página](#formas-de-integrar-código-css-a-nuestra-página)
- [2. Selectores](#2-selectores)
  - [Selector de etiqueta](#selector-de-etiqueta)
  - [Selectores de clase & ID](#selectores-de-clase--id)
  - [Selectores avanzados](#selectores-avanzados)
  - [Agrupar estilos y comentar el código](#agrupar-estilos-y-comentar-el-código)
- [3. Background](#3-background)
  - [Background-Color](#background-color)
  - [Background-image and Background-repeat](#background-image-and-background-repeat)
  - [Background-Position](#background-position)
  - [Gradients](#gradients)
  - [Radial Gradient](#radial-gradient)
- [4. Colores](#4-colores)
  - [ColorName y Hexadecimal](#colorname-y-hexadecimal)
  - [RGB y RGBA](#rgb-y-rgba)
  - [HSL y HSLA](#hsl-y-hsla)
  - [Herramientas imprescindibles para la web](#herramientas-imprescindibles-para-la-web)
- [5. Bordes](#5-bordes)
  - [Bordes](#bordes)
  - [Border Style y Border color](#border-style-y-border-color)
  - [Border Radius](#border-radius)
- [6. Fuentes](#6-fuentes)
  - [Fuentes](#fuentes)
  - [White Space](#white-space)
  - [Word Spacing](#word-spacing)
  - [Text formating](#text-formating)
  - [Text Shadow](#text-shadow)
- [7. Posiciones](#7-posiciones)
  - [Posiciones](#posiciones)
  - [Relative](#relative)
  - [Fixed](#fixed)
  - [Absolute](#absolute)
- [8. Margin & Padding](#8-margin--padding)
  - [Padding](#padding)
  - [Margin](#margin)
  - [Auto Values](#auto-values)
- [9. Imágenes](#9-imágenes)
  - [Imágenes con bordes redondeados](#imágenes-con-bordes-redondeados)
  - [Thumbnails](#thumbnails)
  - [Imágenes responsivas](#imágenes-responsivas)
  - [Efecto Polaroid](#efecto-polaroid)
  - [Filtros](#filtros)
  - [Agregar texto a imágenes](#agregar-texto-a-imágenes)
- [10. Animaciones](#10-animaciones)
  - [Transforms](#transforms)
  - [Transiciones](#transiciones)
  - [Animation](#animation)
  - [Animation pt.2](#animation-pt2)
- [11. Extras](#11-extras)
  - [Pointer events](#pointer-events)
  - [Media Queries](#media-queries)
  - [Media Queries pt.2](#media-queries-pt2)
  - [Pseudo-Clases pt1](#pseudo-clases-pt1)
  - [Pseudo-Clases pt2](#pseudo-clases-pt2)
  - [Pseudo elementos](#pseudo-elementos)
  - [Ejemplos de Frameworks CSS](#ejemplos-de-frameworks-css)
- [12. Ejercicios](#12-ejercicios)
  - [Ejercicios CSS Efecto Paralax](#ejercicios-css-efecto-paralax)
  - [Galeria responsiva](#galeria-responsiva)
  - [Imágenes modal pt1](#imágenes-modal-pt1)
  - [Imágenes modal pt2](#imágenes-modal-pt2)
  - [NavBar CSS pt1](#navbar-css-pt1)
  - [NavBar CSS Agregando estilos pt2](#navbar-css-agregando-estilos-pt2)
  - [NavBar CSS Funcionalidad pt3](#navbar-css-funcionalidad-pt3)
- [13. Flexbox](#13-flexbox)
  - [Qué es Flexbox](#qué-es-flexbox)
  - [Ejes en Flexbox](#ejes-en-flexbox)
  - [Flex Direction](#flex-direction)
  - [Flex Wrap y Flex Flow](#flex-wrap-y-flex-flow)
  - [La propiedad Flex](#la-propiedad-flex)
  - [Justify Content](#justify-content)
  - [Align Items](#align-items)
  - [Centrado vertical y horizontal (práctica)](#centrado-vertical-y-horizontal-práctica)
  - [Align self](#align-self)
- [14. CSS Grid](#14-css-grid)
  - [Qué es el CSS Grid](#qué-es-el-css-grid)
  - [Conceptos del CSS Grid](#conceptos-del-css-grid)
  - [CSS Grid explícito e implícito](#css-grid-explícito-e-implícito)
  - [Definir filas y columnas](#definir-filas-y-columnas)
  - [Posicionar elementos en el grid](#posicionar-elementos-en-el-grid)
  - [Nombrando líneas](#nombrando-líneas)
  - [La función repeat](#la-función-repeat)
  - [Unidad flexible: fr](#unidad-flexible-fr)
  - [Grid area](#grid-area)
  - [Alineamiento](#alineamiento)
  - [Ordenamiento](#ordenamiento)
- [15. Clases en vivo](#15-clases-en-vivo)
  - [Escribir CSS Moderno](#escribir-css-moderno)

# 1. Introducción

## Introducción a CSS

Lenguage en cascada

W3C | Creadores de la estandar de las paginas web. 1996 css esoficial

## Selectores CSS

Selector
Elemento
ID `#titulo`
Clase `.titulo`

Propiedad
`.titulo{color:blue}`

  
## Formas de integrar código CSS a nuestra página

Formas de añadir css en html:
- En línea
- `<style></style>` dentro de html
- Archivo externo

# 2. Selectores

## Selector de etiqueta

```css
h1, p {
  color: green;
  text-align: center;
}
/* clase */

/* 
.ejemplo {
  background-color: pink;
  height: 40px;
  text-align: center;
} */

span h2, p {
  color: red;
  font-size: 30px;
}
```

## Selectores de clase & ID

Selectores clase


``` HTML
 <p class="ejemplo">El curso premiun se encuntra libre</p>
  
  <!-- clase css -->
  <h2 class="ejemplo1">Hola desde H2</h2>
```

Selectores clase 

``` CSS
/* CSS */
/* selector clase */
h2.ejemplo1 {
  color: green;
  height: 40px;
}

/* span h2, p {
  color: red;
  font-size: 30px;
} */
```


selector id en html

```html
  <div id="colores">
    <ul>
      <li id="orange">Orange</li>
      <li id="green">Green </li>
      <li id="red">Red</li>
    </ul>
  </div>
```

Selector id en css

``` CSS

#colores {
  background-color: pink;
  color: violet;
  font-size: 2em
}

#orange {
  color: yellow;
}

#green {
  color: black;
}

#red {
  color: white;
}
```


## Selectores avanzados

``` HTML
<!-- HTML -->
  <div id="colores">
    <ul>
      <li id="orange">Orange</li>
      <li id="green">Green </li>
      <li id="red">Red</li>
    </ul>

  <!-- Selectores de atributos y padres -->
  <p>parrafo</p>
  </div>

  <a href="codigofacilito.com">codigofaclito</a>  
  <a href="animefenix.com">fenix</a>
```

Selectores avanzados en `css`

``` CSS
/* CSS */
#colores > p {
  background-color: pink;
  color: violet;
  font-size: 2em
}

/* nietos */
/* #colores > ul > li {
  background-color: pink;
  color: violet;
  font-size: 2em
} */

a[href="animefenix.com"] {
  color: gold;
}

/* class */

a[class="ejemplo1"]{
  color: violet;
}
```

## Agrupar estilos y comentar el código

1. Regla para modificar el codigo
2. Comentar codigo
3. Ordenar los selectores de etiqueta en css 
4. 


# 3. Background

## Background-Color

``` CSS
/* CSS */
.ejemplo {
  background-color: pink;
  height: 40px;
  text-align: center;
}
```
``` HTML
<!-- HTML -->
  <h1>Hola desde CodigoFacilito, hey</h1>

  <p class="ejemplo">El curso premiun se encuntra libre</p>
```


## Background-image and Background-repeat

``` CSS
/* CSS */
body {
  background-image: url('img/bg_12.jpg');
  background-repeat: no-repeat;
  background-color: black;
}
```

## Background-Position

``` CSS
/* CSS */
body {
  background-image: url('img/bg_12.jpg');
  background-repeat: no-repeat;
  background-color: black;
  /* background-position: right top; */
  /* background-position: center top; */
  background-position: 50% 50%;
  background-attachment: fixed;
  /* background-size: 50% 50%; */
  /* background-size: cover; */
  background-size: 100px 100px;

}
.space {
  height: 600px;
}

```


## Gradients

css

``` CSS
/* CSS */
body {
  background-image: url('img/bg_12.jpg');
  background-repeat: no-repeat;
  background-color: black;
  /* background-position: right top; */
  /* background-position: center top; */
  background-position: 50% 50%;
  background-attachment: fixed;
  /* background-size: 50% 50%; */
  /* background-size: cover; */
  background-size: 100px 100px;
  /* gradient */
  /* background: linear-gradient(to right, gold, yellow, black,violet); */


}
.space {
  height: 600px;
}
```

html
``` HTML
<!-- HTML -->
<body>
  <h1>Curso de CSS</h1>
  <div class="space"></div>
  <div class="space"></div>
  <div class="space"></div>
</body>
```

## Radial Gradient

html

``` HTML
<!-- HTML -->
<body>
  <h1>Curso de CSS</h1>
  <div class="space"></div>
  <div class="space"></div>
  <div class="space"></div>
</body>
```

css

``` CSS
/* CSS */
body {
  background-image: url('img/bg_12.jpg');
  background-repeat: no-repeat;
  background-color: black;
  /* background-position: right top; */
  /* background-position: center top; */
  background-position: 50% 50%;
  background-attachment: fixed;
  /* background-size: 50% 50%; */
  /* background-size: cover; */
  background-size: 100px 100px;
  /* gradient */
  /* background: linear-gradient(to right, gold, yellow, black,violet); */
  /* background: linear-gradient(45deg, gold, yellow, black,violet); */
  /* background: linear-gradient(-80deg, rgba(255, 0, 0, 0), rgba(255, 0, 0, 1)); */
  /* background: linear-gradient(-80deg, red 10%, yellow 40%, green 60%); */
  /* background: radial-gradient(red 5%, yellow 15%, green 60%); */
  background: repeating-radial-gradient(circle, red, yellow, green);
}

.space {
  height: 600px;
}
```

# 4. Colores

## ColorName y Hexadecimal

``` CSS

/* CSS */

h1 {
  /* Name */
  /* background-color: cyan; */
  /* Hexadecimal */
  background-color: #D2691E;
  color: gold;
}
```

## RGB y RGBA

``` HTML
<!-- HTML -->
<body>
  <h1>Colores en css rgb y rgba</h1>
</body>
```

css 

``` CSS
/* CSS */
h1 {
  text-align: center;
  /* color: rgb(0, 0, 255); */
  background-color: rgba(0,0,0,0.6);
  color:white;
}

body {
  background-color: rgba(0,0,0,.5);
}

```

## HSL y HSLA

html

``` HTML
<!-- HTML -->
<body>
  <h1>Colores en css: hsl</h1>
</body>
```
css 

``` CSS
/* CSS */
h1 {
  /* hsl */
  /* background-color: hsl(180,50%,50%) */
  /* hsla */
  background-color: hsl(180,50%,50%,.5)
}
```

## Herramientas imprescindibles para la web

- [adove color](https://color.adobe.com/create)
- [ColorZilla](https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp?hl=es-419Tags)
- [colors.co](https://coolors.co/f5e6e8-d5c6e0-aaa1c8-967aa1-192a51)
- [Foter](https://foter.com/)

# 5. Bordes

## Bordes

html

``` HTML
<body>
  <h1>Bordes en CSS</h1>
</body>
```

css

``` CSS
h1 {
  background-color: hsla(50,100%,50%,.5);
  /* border: solid red 10px; */
  border: dashed rgba(0, 0, 0,.7) 5px;
  border-radius: 5px;
}
```


## Border Style y Border color

html
``` HTML
<body>
  <h1>Bordes en CSS</h1>
</body>
```

css
``` CSS
h1 {
  background-color: hsla(50,100%,50%,.5);
  /* border: solid red 10px; */
  border-top-style:  dashed;
  border-left-style:  dotted;
  border-bottom-color: blue;

}
```


## Border Radius

html

``` HTML
<body>
  <h1>Bordes en CSS</h1>
</body>
```

css 

``` CSS
h1 {
  background-color: hsla(50,100%,50%,.5);
  /* border: solid red 10px; */
  border-top-style:  dashed;
  /* border-left-style:  dotted; */
  /* border-bottom-color: blue; */

  /* border-bottom: dotted blue 10px; */
  border: double #000 25px;
  /* border-radius: 20px; */
  border-radius: 25px;


}
```


# 6. Fuentes

## Fuentes
## White Space
## Word Spacing
## Text formating
## Text Shadow

# 7. Posiciones

## Posiciones
## Relative
## Fixed
## Absolute

# 8. Margin & Padding

## Padding
## Margin
## Auto Values

# 9. Imágenes

## Imágenes con bordes redondeados
## Thumbnails
## Imágenes responsivas
## Efecto Polaroid
## Filtros
## Agregar texto a imágenes

# 10. Animaciones

## Transforms
## Transiciones
## Animation
## Animation pt.2

# 11. Extras

## Pointer events
## Media Queries
## Media Queries pt.2
## Pseudo-Clases pt1
## Pseudo-Clases pt2
## Pseudo elementos
## Ejemplos de Frameworks CSS

# 12. Ejercicios

## Ejercicios CSS Efecto Paralax
## Galeria responsiva
## Imágenes modal pt1
## Imágenes modal pt2
## NavBar CSS pt1
## NavBar CSS Agregando estilos pt2
## NavBar CSS Funcionalidad pt3

# 13. Flexbox

## Qué es Flexbox
## Ejes en Flexbox
## Flex Direction
## Flex Wrap y Flex Flow
## La propiedad Flex
## Justify Content
## Align Items
## Centrado vertical y horizontal (práctica)
## Align self

# 14. CSS Grid

## Qué es el CSS Grid
## Conceptos del CSS Grid
## CSS Grid explícito e implícito
## Definir filas y columnas
## Posicionar elementos en el grid
## Nombrando líneas
## La función repeat
## Unidad flexible: fr
## Grid area
## Alineamiento
## Ordenamiento

# 15. Clases en vivo

## Escribir CSS Moderno