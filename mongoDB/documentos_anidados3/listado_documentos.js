// elimiar elementos de listas
db.users.updateMany(
  {
    courses: {$exists: true}
  },
  {
    $unset: {
      courses: true
    }
  }
)


// agregar nuevos elementos a las listas
db.users.updateOne(
  {
    name: 'Victor'
  },
  {
    $set: {
      courses: [
        {
          title: 'JavaScript',
          progress: 40,
          completed: false
        },
        {
          title: 'Docker',
          progress: 100,
          completed: true
        },
        {
          title: 'Git',
          progress: 100,
          completed: true
        }
      ]
    }
  }
)
