//$elemMatch
//obtener todos los usuarios que hayan completado por lo menos un curso
db.users.find(
  {
    courses: {
      $elemMatch: {
        completed: true
      }
    }
  }
).pretty()

//Obtener todos los usurios con un progreso de 80
//$elemMatch -> ingresamos a los elentos de las lista para obtener las datos, sin ningun problema
db.users.find(
  {
    courses: {
      $elemMatch: {
        progress: {$gte: 80}
      }
    }
  }
)

//obtener el nombre del usurio junto con el titulo de cada uno de sus cursos -> deseamos a Obtenera
db.users.find(
  {
    courses: {$exists: true}
  },
  {
    _id: false,
    name: true,
    'courses.title': true
  }
).pretty()
