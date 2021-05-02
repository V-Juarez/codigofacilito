// Obtener todos los usuarios cuya edad sea mayor a 20
db.users.find(
  {
    age: {
      $ge: 25       //representa a mayor que >
    }
  }
)

// Obtener todos los usuarios cuya edad sea mayor a 20
db.users.find(
  {
    age: {
      $gte: 25       //representa a mayor que >=
    }
  }
)

// Obtener todos los usuarios cuya edad sea mayor a 20
db.users.find(
  {
    age: {
      $lte: 25       //representa a sea menor que >=
    }
  }
)

// $gt >
// $gte >=
// $lt <
// $lte <=
// $eq ==
// $ne !=
