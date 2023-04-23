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
enlistarCamaras();

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

async function enlistarCamaras() {
  let camarasDisponibles = await navigator.mediaDevices.enumerateDevices();
  camarasDisponibles = camarasDisponibles.filter(device => device.kind === "videoinput")
  let select = document.createElement('select')

  camarasDisponibles.forEach(camara => {
    let option = document.createElement('option')
    option.innerHTML = camara.label;
    option.value = camara.deviceId;
    select.appendChild(option);
  });

  select.addEventListener('change', function(ev) {
    solicitarPermisosCamara(select.value)
  })
  document.querySelector('body').appendChild(select)
  console.log(camarasDisponibles)
}

// Solcitar permisos para la camara => Leer la camara y mostrarla en el video
async function solicitarPermisosCamara(deviceId) {
  // getUserMedia

  let constrainst = {};
  if(deviceId) {
    constrainst = {
      video: { deviceId: deviceId }
    }
  } else {
    constrainst = { video: true }
  }
  /*
   * @ getUserMedia => Solicita perisos para la camara y el micro y retorna un
   *   MediaStream
   * */

  let mediaStream = await navigator.mediaDevices.getUserMedia(constrainst);
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
  // context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  drewImageProp(context, video);

  if (imagenCargada) {
    context.drawImage(imagenCargada, 0, 0, canvas.width, canvas.height);
  }

  requestAnimationFrame(dibujar);
}

function drewImageProp(ctx, img, x, y, w, h, offsetX, offsetY) {
  if (arguments.length ===2 ) {
    x = y = 0;
    w = ctx.canvas.width
    h = ctx.canvas.height
  }

  offsetX = typeof offsetX === "number" ? offsetX : 0.5;
  offsetY = typeof offsetY === "number" ? offsetY : 0.5;

  if (offsetX < 0) offsetX = 0;
  if (offsetY < 0) offsetY = 0;
  if (offsetX > 1) offsetX = 1;
  if (offsetY > 1) offsetY = 1;


  var iw = img.videoWidth,
  ih = img.videoHeight,
  r = Math.min(w / iw, h / ih),
  nw = iw * r,
  nh = ih * r,
  cx, cy, cw, ch, ar = 1;

  // decide which gap to fill
  if (nw < w) ar = w /nw;
  if (Math.abs(ar - 1) < 1e-14 && nh < h) ar = h /nh; // updated
  nw *= ar;
  nh *= ar;


  // calc source rectangle
  cw = iw / (nw / w);
  ch = ih / (nh / h);

  cx = (iw - cw) * offsetX;
  cy = (ih - ch) * offsetY;

  // make sure source rectangle is valid
  if (cx < 0) cx = 0;
  if (cy < 0) cy = 0;
  if (cw > iw) cw = iw;
  if (ch > ih) ch = ih;

  // fill image in dest, rectangle
  ctx.drawImage(img, cx, cy, cw, ch, x, y, w, h);
}