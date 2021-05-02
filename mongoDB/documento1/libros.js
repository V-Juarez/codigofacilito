db.books.insertMany(
        [
            {title: 'Don Quijote de la Mancha', sales: 500},
            {title: 'Soy un Gato', sales: 100},
            {title: 'Historia de las Ciudades', sales: 150},
            {title: 'El aniloo', sales: 800},
            {title: 'El principito', sales: 500},
            {title: 'The Maker', sales: 600},
            {title: 'Castillo', sales: 400},
            {title: 'Iliada', sales: 650},
            {title: 'El Gran vendedor', sales: 250},
            {title: 'Pience y Hagase ser Rico', sales: 1000}
        ]
)


// like -> expression regular
// Obtener todos los libros cuyo titulo comiencen con El
// Obtener todos los libros cuyo titulo finalicen con s
// Obtener todos los libros que posean en su titulo la palabra la

// WHERE title LIKE 'El%'

db.books.find(
  {
    title: /^El/
  }
)

// WHERE title LIKE '%s'
db.books.find(
  {
    title: /s$/
  }
)

// WHERE title LIKE '%la%'
db.books.find(
  {
    title: /la/
  }
)

//Obtener todos los usuarios sean Victor o Fernando o Gabriela

db.users.find(
  {
    $or: [
      {
        name: 'Victor'
      },
      {
        name: 'Fernando'
      },
      {
        name: 'Gabriela'
      }
    ]
  }
)

// bucar valores dentro de una lista
db.users.find(
  {
    name: {
      $in: ['Victor', 'Fernando', 'Gabriela']
    }
  }
).pretty()

//buscar valores que no se encuentran en la lista
db.users.find(
  {
    name: {
      $nin: ['Victor', 'Fernando', 'Gabriela', 'Rafael']
    }
  }
).pretty()
