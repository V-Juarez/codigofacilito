// id
const title = document.getElementById('title');
title.innerHTML = 'Cursos';

const description = document.getElementById('description');
description.innerHTML = "Listado de cursos";

// class
// const items = document.getElementsByClassName('list-group-item');
// for (var i = 0; i < items.length; i++) {
//   let element = items[i];
//   console.log(element)
// }

// etiqueta
const items = document.getElementsByTagName('li');
for (var i = 0; i < items.length; i++) {
  if (i % 2 == 0) {
    let element = items[i];
    element.style.background = '#f2f2f2'
    console.log(element)
  }
}
