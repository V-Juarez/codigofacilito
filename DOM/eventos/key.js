const input = document.getElementById('input')

input.addEventListener('keydown', function(e){
  console.log('tecla press', e.key + ' con un codigo  ' + e.keyCode)
})