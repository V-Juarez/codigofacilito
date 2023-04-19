const button = document.querySelector(".btn.btn-primary");

// click -> 1 | dblclick -> 2
button.addEventListener("click", function (e) {
  console.log(e)
  if(title.style.display != 'none') {
    title.style.display = 'none'
    description.style.display = 'none'
    // button.textContent = 'Mostrar'
    e.target.textContent = 'Mostrar'
    this.textContent = 'mostrar'
  } else {
    title.style.display = 'block'
    description.style.display = 'block'
    // button.textContent = 'Ocultar'
    // e.target.textContent = 'Ocultar'
    this.textContent = 'Ocultar'
  }
});
