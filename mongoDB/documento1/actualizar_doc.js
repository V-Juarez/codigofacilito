var Gabriela = db.users.findOne(
  {name: 'Gabriela'}
)

Gabriela.support = true
// argumento un documento, si el documento posee el attr id -> update -> create
db.users.save(Gabriela)


//Obtener un solo documento
var Gabriela = db.users.findOne(
  {name: 'Gabriela'}
)

//Actualizar documetos
//updateOne o updateMany
db.users.updateMany(
  {
    support: {
      $exists: false
    }
  },
  {
    $set: {
      support: false
    }
  }
)

//updateOne actualiza al documento que cumpla la condicion
db.users.updateOne(
  {
    name: 'Gabriela'
  },
  {
    $set: {
      support: false
    }
  }
)

//Elimiar atributos de nuestro documento
db.users.findOne(
  {
    createdAt: {$exists: true}
  },
  {
    $unset: {createdAt: true}
  }
)

//Actualizar los atributos de los documetos
db.users.updateOne(
  {
    createdAt: {$exists: true}
  },
  {
    $unset: {createdAt: true}
  }
)


// incrementar atributos del documento $inc -> int

db.users.updateOne(
  {
    name: 'Gabriela'
  },
  {
    $inc: {
      age: -1
    }
  }
)
