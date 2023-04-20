const button = document.querySelector('.btn.btn-primary')

button.addEventListener('click', function() {
  
  button.addEventListener(' mouseenter', function(){
    this.className = 'btn btn-danger'
  })
  button.addEventListener('mouseout', function(){
    this.className = 'btn btn-primary'
  })
})

