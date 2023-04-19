const title = document.getElementById("title");
title.innerHTML = "Cursos";

const description = document.getElementById("description");
description.textContent = "Listado de cursos";

const button = document.querySelector(".btn.btn-primary");

// click -> 1 | dblclick -> 2
button.addEventListener("dblclick", function () {
  console.log("Hola mundo");
});
