// $limit y $sort
// Obtener al usuario mas joven
db.users.aggregate(
  [
      {
          $sort: {
              age: 1
            }
        },
          {
            $limit: 1
          },
        {
            $project: {
              _id:false, name:true, age:true
          }
      }
  ]
)
