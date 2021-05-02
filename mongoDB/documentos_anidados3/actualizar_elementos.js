// actualizar elementos
db.users.updateOne(
  {
    name: 'Gabriela'
  },
  {
    $set: {
      'address.number': 20,
      'address.number': [
        'Fuera de la casa se encuentra un pajaro',
        'Fuera de la casa se encuentra un pino (arbol)'
      ],
    }
  }
)

//2
db.users.updateOne(
  {
    name: 'Victor'
  },
  {
    $set: {
      'address.number': 21002,

    }
  }
)

// 2
db.users.updateOne(
  {
    name: 'Raul'
  },
  {
    $push: {
      'address.references': {
        $each: [
          'Fuera de la casa hay un rio',
          'Fuera de la casa hay un campo de futbol'
        ]
      }
    }
  }
)

//3
