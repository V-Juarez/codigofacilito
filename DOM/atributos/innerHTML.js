const description = document.getElementById('description');

// modificar un nodo 
description.textContent = 'Listado de cursos: '

// modificar un elemento
description.innerHTML = '<strong>' + description.textContent + '</strong>';