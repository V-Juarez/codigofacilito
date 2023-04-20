const form = document.getElementById('course-form')

form.addEventListener('submit', function(e){
  e.preventDefault();
  
  let title = document.getElementById('title-form').value;
  let description = document.getElementById('description-form').value;
  console.log(title)
  console.log(description)
});