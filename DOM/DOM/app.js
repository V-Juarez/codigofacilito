const title = document.getElementById('title')
title.innerHTML = 'Cursos'

const description = document.getElementById('description')
description.textContent = 'Listado de cursos'

const items = document.querySelectorAll('li:nth-child(even)');

for(let element of document.querySelectorAll('*')){
  element.addEventListener('click', show_messages)
}

const row = document.querySelector('.row')
const form = document.getElementById('course-form')

form.addEventListener('submit',  function(e) {
  e.preventDefault();

  let title = document.getElementById('title-form').value;
  let description = document.getElementById('description-form').value;

  create_card(title, description);
})

function create_card(title, description) {
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