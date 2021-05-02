// $group

db.items.insertMany(
  [
    {type: 'Camera', color: 'Red', price: 120},
    {type: 'Laptop', color: 'While', price: 120},
    {type: 'Laptop', color: 'Black', price: 120},
    {type: 'Camera', color: 'Silver', price: 120},
    {type: 'Microphone', color: 'Black', price: 120},
    {type: 'Mouse', color: 'While', price: 50},
    {type: 'Monitor', color: 'While', price: 50},
  ]
)

//Agrupar y contar la cantidad de items con respecto a su tipo
db.items.aggregate(
  [
    {
      $group: {
        _id: '$type',
        total: { $sum: 1 }
      }
    },
    {           //having
      $match: {
        total: {$gt: 1}
      }
    }
  ]
)
