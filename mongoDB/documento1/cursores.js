// find -> retorna un crusor
//it nos permite visualizar los demas documentos

for(i = 0; i < 100; i++){
  db.demo.insert(
    {name: 'user' + 1}
  )
}

// count() -> obtener todos los usuarios con correo electronico
db.users.find(
  {
    email: /mytacam78@gmail.com$/
  }
).count()

//limit()-> cantidad de documentos debemos obtener
db.users.find().limit(2)

// skip() -> Obtener el tercer usuario de la coleccion usuarios | podemos combinar .skip().limit()
db.users.find().skip(3).limit(1)

//sort() -> Obtener el nombre de todos los usuarios ordenados alfabeticamente
db.users.find(
  {},
  {
    _id:false, name: true
  }
).sort(
  {
    name: 1
  }
) // 1 asendente
// -1 desendente

//Obtener el tercer usuario ordenado por su nombre de forma desendente
db.users.find().sort({
  name: -1
}).skip(2).limit(1)

//findOne-> retorna un documento
//find -> retorna un crusor


//findAndModify: retorna los datos antes de actualizarlos
db.users.findAndModify(
  {
      //sort, remove, upsert
      query: {
        name: 'Pablo'
      },
      update: {
          $inc: {
            age: 1
        }
      },
      new: true
  }
)
