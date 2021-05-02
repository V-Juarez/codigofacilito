// buscar elementos dentro de las listas y obtener los usuarios cursos -MongoDB o SQL> $all
db.users.find(
  {
    courses: {
      $all: ['SQL','MongoDB','Python']
    }
  }
).pretty()


//Obtener todos los usuarios con los cursos MongoDB o SQL
db.users.find(
  {
    courses: 'MongoDB'
  }
)

//$and
db.users.find(
  {
    $and: [
      {
        courses: 'SQL'
      },
      {
        courses: 'MongoDB'
      }
    ]
  }
)

//$or obtine el elemento y muestra el documento
db.users.find(
  {
    $or: [
      {
        courses: 'Git'
      },
      {
        courses: 'MongoDB'
      }
    ]
  }
).pretty()
