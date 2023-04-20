const title = document.getElementById('title')
title.innerHTML = 'Cursos'

const description = document.getElementById('description')
description.textContent = 'Listado de cursos'

const items = document.querySelectorAll('li:nth-child(even)');

for (var i = 0; i < items.length; i++) {

}
const row = document.querySelector('.row')
const form = document.getElementById('course-form')

form.addEventListener('submit',  function(e) {
  e.preventDefault();

  let title = document.getElementById('title-form').value;
  let description = document.getElementById('description-form').value;

  create_card(title, description);
})

function create_card_by_innerHTML(title, description) {
  let html = `
    <div class="col-sm-6 col-md-4">
      <div class="thumbnail">
        <div class="caption">
          <h3 id="title_card">${title}</h3>\
          <p id="description_card">${description}</p>\
          <p>
            <a href="#" class="btn btn-danger">Accion</a>
          </p>
        </div>
      </div>
    </div>
  `;
  row.innerHTML += html;
}

function create_card(title, description){
  let div = document.createElement('div');
  div.className = 'col-sm-6 col-md-4';

  let thumbnail = document.createElement('div')
  thumbnail.className = 'thumbnail'

  let caption = document.createElement('div')
  caption.className = 'caption'

  let h3 = document.createElement('h3')
  h3.textContent = title;

  let p1 = document.createElement('p')
  p1.textContent = description
  
  let p2 = document.createElement('p')
  let a = document.createElement('a')
  a.className = 'btn btn-danger'

  a.textContent = 'eliminar'

  // agregar methos
  p2.appendChild(a)
  caption.appendChild(h3)
  caption.appendChild(p1)
  caption.appendChild(p2)

  thumbnail.appendChild(caption)
  div.appendChild(thumbnail)


  row.appendChild(div)
}
