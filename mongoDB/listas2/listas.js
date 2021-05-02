//Crear usuarios con cursos
db.users.updateOne(
  {
    name: 'Raul'
  },
  {
      $set: {
          courses: ['Python', 'MongoDB', 'SQL', 'Java']
      }
  }
)

db.users.updateOne(
  {
    name: 'Pablo'
  },
  {
      $set: {
          courses: ['Git', 'Escritura para programadores', 'Redes']
      }
  }
)

// Obtener al usuario que posea los cursos de Python, MongoDB, SQL, Java

db.users.findOne(
  {
    courses: ['Python', 'MongoDB', 'SQL', 'Java']
  }
)

db.users.findOne(
  {
    courses: {
      $eq: ['Python', 'MongoDB', 'SQL', 'Java']
    }
  }
)
