//$and y $or
// Obtener todos los usuarios cuya edad sea mayor a 20 y menor a 26
// $and
db.users.find(
  {
      $and: [
          {
            age: {$gt: 20}
          },
          {
            age: {$lt: 26}
          }
      ]
  }
).pretty()


//$or
//Obtener todos los usuarios cuyo nombre sea Victor o Gabriela
db.users.find(
  {
    $or: [
      {
          name: 'Victor'
      },
      {
          name: 'Gabriela'
      }
    ]
  }
).pretty()


// Obtener todos los usuarios cuyo nombre se Victor o Gabriela o la edad sea mayor a 20 y menor a 25
db.users.find(
  {
    $or: [
      {
          name: 'Victor Emily'
      },
      {
          name: 'Gabriela'
      },
      {  $and: [
            {age: {$gt: 20}},
            {age: {$lt: 26}}
        ]
      }
    ]
  }
).pretty()
