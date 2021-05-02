db.autores.find(
  {
    nombre: 'Stephen King'
  }
).explain('executionStats')
