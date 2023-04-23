// DOM API
let video = document.querySelector('.video-source')
// Canvas
let canvas = document.querySelector('#canvas')
let context = canvas.getContext('2d')
let imagenCargada;

async function solicitarPermisosCamara(){
  // getUserMedia
  let mediaStream = await navigator.mediaDevices.getUserMedia({ video: true })
  // API video
  video.srcObject = mediaStream;
  video.play()
}

async function cargarImagen(){
  let image = document.createElement('img')
  image.src = '../image/frame.png'
  await image.decode();
  imagenCargada = image;

  dibujar()
}

function dibujar() {
  if(imagenCargada){
    context.drawImage(imagenCargada, 0, 0, 100, 200)
  }

}

solicitarPermisosCamara();
cargarImagen();
dibujar();

