// Relacion uno a uno
var usuario = {
  nombre: 'Leonel',
  apellido: 'Dominguez',
  edad: 27,
  correo: requel@example.com,
  direccionPostal: {
    calle: 'Calle',
    ciudad: 'ciudad',
    estado: 'estado',
    codigoPostal: 1,
    numeroext: 10
  }
}

db.users.insertOne(usuario)

//

var autor = {
  nombre: 'Stephen King',
  nacionalidad: 'Estadounidense',
  libros: [
            {
            titulo: 'it',
            fechalanzamiento: 1986
          },
          {
          titulo: 'Respandor',
          fechalanzamiento: 1977
        },
        {
        titulo: 'Misery',
        fechalanzamiento: 1987
      }
  ]
}

// Llaves foraneas -> objectsId
var autor = {
  nombre: 'Stephen King',
  nacionalidad: 'Estadounidense'
}

db.autores.insertOne(autor)

//

var libro1 = {
  titulo: 'it',
  fechalanzamiento: 1986,
  autor_id: ObjectId("5ed5db3638d301bf3c4144d1") //llave foranea
}

var libro2 = {
  titulo: 'Respandor',
  fechalanzamiento: 1977,
  autor_id: ObjectId("5ed5db3638d301bf3c4144d1") //llave foranea
}

var libro3 = {
  titulo: 'Misery',
  fechalanzamiento: 1987,
  autor_id: ObjectId("5ed5db3638d301bf3c4144d1") //llave foranea
}

db.libros.insertMany(
  [
    libro1, libro2, libro3
  ]
)

//-------------------------------------//
db.users.createIndex(
  {autor_id: 1}
)


db.autores.insertMany(
  [
    {nombre: 'J.K', nacionalidad: 'Britanica'},
    {nombre: 'Gerorge', nacionalidad: 'Estadounidense'}
  ]
)

db.libros.insertMany(
  [
      {
        titulo: 'Harry Poter y la piedra',
        fechalanzamiento: 1997,
        autor_id: ObjectId("5ed5db3638d301bf3c4144d1")
      },
      {
        titulo: 'Henry Ford',
        fechalanzamiento: 1999,
        autor_id: ObjectId("5ed5db3638d301bf3c4144d1")
      }
  ]
)

//obtener todos los autores con su correspondiente listado de libros
db.autores.aggregate(
  [
      {
          $lookup: {
            from: 'libros',
            localfield: '_id',
            foreingField: 'autor_id',
            as: 'listadoLibros'
          }
      },
      {
        $match: {
          listadoLibros: {
            $ne: []
          }
        }
      },
      {
        $project: {
          _id:false, nombre:true
        }
      }
  ]
).pretty()

//obtener todos los autores que poseean un libro1



//--------------------------//--------------------------------------//----------//
