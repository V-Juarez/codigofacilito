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
  }
}

// elemento css
// id
const element = document.querySelector('#first-course');
console.log(element);

// class
const element1 = document.querySelector('.list-group-item');
console.log(element1);

// tag
const element2 = document.querySelector('li');
console.log(element2);

// reglas de ccs
const element3 = document.querySelector('div.row > ul.list-group > li');
console.log(element3);


// querySelectoAll
// par odd
// impart even
const items1 = document.querySelectorAll('li:nth-child(even)')
for (var i = 0; i < items1.length; i++){
  let element = items1[i]
  element.style.background = 'gray';
}
