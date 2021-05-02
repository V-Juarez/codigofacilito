//
db.users.find(
  {
    age: {$gt: 24}
  }
)

///1
db.users.aggregate(
  [
    {
      $match: {
        age: {$gt: 24} // 3
      }
    },
    {
      $match: {
        courses: {$exists: true}  //and
      }
    },
      {
        $match: {
          lastName: 'Gonzalez'
        }
      }
  ]
).pretty()
