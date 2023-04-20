const element =  document.querySelector('li')
const list = document.querySelector('ul')
const div_row = document.querySelector('.row')
const div_container = document.querySelector('.container')
const body = document.querySelector('body')

element.addEventListener('click', function() {
  console.log('Elemento')
})
list.addEventListener('click', function(e) {
  console.log('Lista')
  e.stopPropagation();
})
div_row.addEventListener('click', function(e) {
  console.log('Div Row')
  e.stopPropagation();
})
div_container.addEventListener('click', function(e) {
  console.log('Div container')
  e.stopPropagation();
})
body.addEventListener('click', function(e) {
  console.log('body')
  e.stopPropagation();
})


/* element.addEventListener('click', show_messages, e);
list.addEventListener('click', show_messages);
div_row.addEventListener('click', show_messages);
div_container.addEventListener('click', show_messages);
body.addEventListener('click', show_messages); */


/* for(let element of document.querySelectorAll('*')){
  element.addEventListener('click', show_messages)
} */

function show_messages(e) {
  console.log("Elemento actual", this.tagName)
  console.log("Elemento que disparo el evento", e.target.tagName)
}