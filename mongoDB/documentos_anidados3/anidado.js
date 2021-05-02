db.users.updateOne(
  {
    name: 'Raul'
  },
  {
    $set: {
      address: {
        state: 'CDG',
        city: 'CDG',
        number: 10,
        street: 'Calle numero 1',
        postalCode: 1,
        references: ['Casa Grande', 'aun costado de un tienda De zapatos']
      }
    }
  }
)

//obeter abributos en documentos
//obtener todos los usuarios que poseean un direccion postalCode
db.users.find(
  {
    addres: { $exists: true}
  }
)

// Obtener todos los usuarios que posean un codigo postalCode 1 y un numero igual a 10
// 1
db.users.find(
  {
    'address.postalCode': 1
  }
).pretty()

// 2
db.users.find(
  {
    $and: [
      {
        'address.postalCode': 1
      },
      {
        'address.number': {$exists: true}
      },
      {
        'address.number': {$gte: 10 }
      },
    ]
  }
).pretty()


// Obtener la primera referencia de los usuarios con codigo pastal y references
db.users.find(
  {
    $and: [
      {
        address: {$exists: true}
    },
    {
      'address.references': {$exists: true}
    },
  ]
},
{
    _id: false,
    name: true,
    'address.references': {
      $slice: 1
    }
}
)
