// DOM API
let video = document.querySelector(".video-source");
// Canvas
let canvas = document.querySelector("#canvas");
let context = canvas.getContext("2d");
let botonFoto = document.querySelector("#botton-foto");

// Definir una variable vacia
let imagenCargada;

redimensionarCanvas();
solicitarPermisosCamara();
cargarImagen();
dibujar();

botonFoto.addEventListener("click", function (ev) {
  let url = canvas.toDataURL("image/jpeg");
  let a = document.createElement("a");
  a.href = url;
  a.innerHTML = "Descargar";
  document.querySelector("body").appendChild(a);
  a.download = "foto.jpg";
  a.click();
});

function redimensionarCanvas() {
  let camara = document.querySelector(".camara");
  canvas.width = camara.clientWidth;
  canvas.height = camara.clientHeight;
}

// Solcitar permisos para la camara => Leer la camara y mostrarla en el video
async function solicitarPermisosCamara() {
  // getUserMedia
  /*
   * @ getUserMedia => Solicita perisos para la camara y el micro y retorna un
   *   MediaStream
   * */

  let mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
  // API video
  //
  // Stream sera la fuente de dattos para el elemento video
  video.srcObject = mediaStream;
  // reporducir el video con Javascript
  video.play();
}

async function cargarImagen() {
  // node img
  let image = document.createElement("img");
  // asignar el frame
  image.src = "../image/frame.png";
  // descarga la imagen
  await image.decode();
  // guarda la imagen en la varialle
  imagenCargada = image;
}

function dibujar() {
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  if (imagenCargada) {
    context.drawImage(imagenCargada, 0, 0, canvas.width, canvas.height);
  }

  requestAnimationFrame(dibujar);
}
