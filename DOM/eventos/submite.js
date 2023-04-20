const form = document.getElementById('course-form')

form.addEventListener('submit', function(e){
  e.preventDefault();
  
  let title = document.getElementById('title-form').value;
  let description = document.getElementById('description-form').value;
  console.log(title)
  console.log(description)
});

const checkbox = document.getElementById('checkbox')
let title_form = document.getElementById('title-form')

title_form.addEventListener('change', function() {
  console.log('Cambo de valor' )
})