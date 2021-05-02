//Obtener el promedio de los usuarios
db.users.aggregate(
  {
    $match: {
      scores: {$exists: true}
    }
  },
  {
    $project: {
      _id:false, name:true, scores:true
    }
  },
  {
    $set: {                           //error en el codigo
      sum: { $sum: '$scores' }
    }
  },
  {
    $set: {
      avg: {$avg: '$scores' }
    }
  },
  {
    $match: {
      avg: {$gt: 7}
    }
  }
)
