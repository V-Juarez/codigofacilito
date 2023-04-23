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
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  if (imagenCargada) {
    context.drawImage(imagenCargada, 0, 0, canvas.width, canvas.height);
  }

  requestAnimationFrame(dibujar);
}
