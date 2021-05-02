// Es cuando conocemos el indice
db.users.updateMany(
  {
    scores: { $exists: true}
  },
  {
    $set: {
      'scores.0': 5
    }
  }
)

// Cuando no conocemos el indice
db.users.updateMany(
  {
    scores: { $exists: true},
    scores: 9
  },
  {
    $set: {
      'scores.$': 6
    }
  }
)

//obtener elementos de una lista $slice por su posicion o indice
db.users.findOne(
  {
    name: 'Pablo'
  },
  {
    _id: false,
    name: true,
    courses: true
  }
)

// 1
db.users.findOne(
  {
    name: 'Pablo'
  },
  {
    _id: false,
    name: true,
    courses: {
      $slice: 2  //int o []
    }
  }
)

// 2
db.users.findOne(
  {
    name: 'Pablo'
  },
  {
    _id: false,
    name: true,
    courses: {
      $slice: [0, 3]  //int o []
    }
  }
)
