//scores -> agrecar calificacion
db.users.updateOne(
  {
    name: 'Gabriela'
  },
  {
    $set: {
      scores: [9, 8, 9, 5, 10]
    }
  }
)

db.users.updateOne(
  {
    name: 'Raul'
  },
  {
    $set: {
      scores: [9, 3, 2, 10, 10]
    }
  }
)

// obtener todos los usuarios que posean por lo menos una calificacion de 10
db.users.find(
  {
    scores: 10
  }
).pretty()

// obtener todos los usuarios que hayan reprobado por lo menos una calificacion
db.users.find(
  {
    scores: {
      $lt: 6
    }
  }
).pretty()
