// DOM API
let video = document.querySelector('.video-source')

async function solicitarPermisosCamara(){
  // getUserMedia
  let mediaStream = await navigator.mediaDevices.getUserMedia({ video: true })
  // API video
  video.srcObject = mediaStream;
  video.play()
}

async function cargarImagen(){
  
}

solicitarPermisosCamara();

// Canvas

let canvas = document.querySelector('#canvas')
let context = canvas.getContext('2d')

context.fillStyle = 'red'
context.fillRect(40,40,100,200)

