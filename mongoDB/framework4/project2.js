// obtener los 2 primeros cursos con el operador #slice
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
        $project: {
          _id:false, name: true, courses:true
        }
      },
      {
        $project: {
          name:true,        //problemas en esta area de trabajo
          firstCourses: {
            $slice: [ '$courses', 2 ]
          }
        }
      }
    ]
  )


db.users.aggregate(
  [
    {
    $match:{
              $and: [
              {
                name: {$exists: true}
              },
              {
                lastName: {$exists: true}
              }
            ]
          }
        },
      {
        $project: {
          _id:false, name: true, lastName:true
        }
    },
    {
      $project: {
        fullName: {
          $concat: ['$name', ' ', '$lastName']
        }
      }
    }
  ]
)
      },
      {
        $project: {
          name: true,
          course: {
            $arrayElemAt: ['$firstCourses', 0]
          }
        }
      },
      {
        $addFields: {
          currentDate: new Date(),
          newName: '$name'
        }
      }
  ]
).pretty()
