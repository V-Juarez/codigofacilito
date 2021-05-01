
//DOM
// let tabla = document.querySelectorAll("a");
//
// tabla.forEach(function(tabla){
//   console.log(tabla);
// });

/*
let celdas = document.querySelectorAll("td");

celdas.forEach(function(td){
  td.addEventListener('click',function(){
    console.log(this);
  })
});*/

//Obtener los elmentos de la clase .close
let links = document.querySelectorAll(".close");

//Recordarlos
  links.foreach(function(link){

//Agregar un evento click a cada uno de ellos
  link.addEventListener("click",function(ev){
    ev.preventDefault();

    let content = document.querySelectorAll('.content');

    //Quitar las animaciones que ya tienen
    content.classList.remove("fadeInDown");
    content.classList.remove("animate");

    //Agregar clases para animar su salida fadeOutUp

    content.classList.add("fadeOutUp");
    content.classList.add("animate");

    setTimeuot(function(){
      location.href = "/boletines";
    },600);

    return false;

  });
});

let iconos = document.querySelectorAll("i");

iconos.forEach(function(icono){
  icono.classList.remove("fa-star-o");
})
