// upsert -> udpate, crea un nuevo registro/actualiza la existente
db.users.updateOne(
  {
    name: 'Luis'
  },
  {
    $set: {
      age: 20
          }
    },
    {
      upsert: true
    }
)

//elimiar documentos remove({})
db.users.remove(
  {
    name: 'Luis'
  }
)

//Elimina el documento comple
db.books.remove({})

//dropDatabase() -> elimina una base de datos
//drop() nos permite elimiar una coleccion
db.books.drop()
db.dropDatabase()
