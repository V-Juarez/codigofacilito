// insetOne

var user2 = {
  name: 'Fernando',
  last_name: 'Torres',
  age: 25,
  email: 'fernadotorres@gmail.com'
}


db.users.insertOne(user2)

// insertMany - varios documentos
var user1 = {
  name: 'Victor',
  last_name: 'Juarez',
  age: 25,
  email: 'mytacam78@gmail.com'
}

var user2 = {
  name: 'Fernando',
  last_name: 'Torres',
  age: 25,
  email: 'fernadotorres@gmail.com'
}

var user3 = {
  name: 'Pablo',
  last_name: 'Torres',
  age: 25,
  email: 'pablotrr@gmail.com'
}

var user4 = {
  name: 'Raul',
  last_name: 'Gonzalez',
  age: 25,
  email: 'raulgz@gmail.com'
}

var user5 = {
  name: 'Gabriela',
  last_name: 'Rock',
  age: 24,
  email: 'gabrielarck@gmail.com'
}

db.users.insertMany([user1, user2, user3, user4, user5])

db.users.find(
  {age: 25},
  {age: false},
  {name: true, email:true, _id: false}
).pretty()


$ne -> diferente a
$ne -> igual a
//Obtengamos todos los usuarios cuya eda sea direente a 25
db.users.find(
  {
      age: {
        $ne: 25
      }
  }
).pretty()

//Obtengamos todos los usuarios cuya edad sea igual a 25

db.users.find(
  {
      age: {
          $eq: 25
      }
  }
).pretty()


// find > documentos
// findOne > un solo ducumento en la busqueda
db.users.findOne(
  {
      age: {
          $eq: 25
      }
  }
)
