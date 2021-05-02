// $push -> insertar un elementos
db.users.updateOne(
  {
    name: 'Victor'
  },
  {
    $push: {
      courses: 'Python'
    }
  }
)

// $push $each -> Ingresar varios elementos
db.users.updateOne(
  {
    name: 'Gabriela'
  },
    {
      $push: {
        courses: {
          $each: ['Django', 'Rails', 'Rust']
        }
      }
    }
)

// Ingresar y colocarlos varios elementos en la $position que se desea ->  $position
db.users.updateOne(
  {
    name: 'Gabriela'
  },
  {
      $push: {
        courses: {
          $each: ['C#', 'Java', 'Python'],
          $position: 2
        }
      }
  }
)

// $sort ingresar elementos de forma ordenado.
db.users.updateOne(
  {
    name: 'Victor'
  },
  {
    $push: {
      scores: {
        $each: [10, 10, 10, 8, 6, 3, 4],
        $sort: -1
      }
    }
  }
)

// Elimiar elementos
db.users.updateOne(
  {
    courses: { $exists: true}
  },
  {
    $pull: {
      courses: 'Python'
    }
  }
)

db.users.updateMany(
  {
    courses: { $exists: true}
  },
  {
    $pull: {
      courses: 'Python'
    }
  }
)

// elimiar varios elementos
db.users.updateMany(
  {
    courses: { $exists: true}
  },
  {
    $pull: {
      courses: {
        $in: ['Base de Datos', 'C#']
    }
    }
  }
)
