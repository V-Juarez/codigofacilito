// Obtener todos los usuarios con 5 cursos
db.users.find(
  {
    courses: {
      $size: 3
    }
  }
).pretty()


// $where
//Obener todos los usuarios que poseean por lo menos 3 cursos
db.users.find(
  {
    $and: [
      {
        courses: {$exists: true}
      },
      {
        $where: 'this.courses.length >= 3'
      }
    ]
  }
).pretty()
