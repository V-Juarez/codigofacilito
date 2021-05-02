var user6 = {
  name: 'Sandra',
  email: 'san@gmail.com',
  support: true,
  createdAt: new Date()
}

//Obtener todos los usuarios que posean apellidos
db.users.find(
  {
    last_name: {
      $exists: true
    }
  }
)

db.users.find(
  {
    last_name: {
      $exists: false
    }
  }
)

// Obtener todos los usuarios cuyo attr createdAt sea de tipo Date
db.users.find(
  {
    createdAt: {
      $type: 'date'
    }
  }
)

db.users.find(
  {
    $and: [
      {
        createdAt: {$exists: true}
      },
      {
        createdAt: {$type: 'date'}
      }
    ]
  }
)
