// $map
db.users.aggregate(
  [
    {
        $match: {
          scores: { $exists: true }
        }
      },
      {
        $project: {
          _id:false, name:true, scores:true
        }
      },
      {
        $project: {
          name: true,
          scores: true,
            newListScores: {
              $map: {
                input: '$scores',
                as: 'Calificacion',
                in: {
                  $multiply: [ '$$calificacion', 10]
                }
              }
          }
        }
      }
  ]
)


db.users.aggregate(
  [
      {
        $match: {
          courses: {$exists: true}
        }
      },
      {
        $project: {
          _id:false, name:true, courses:true
        }
      },
      {
        $project: {
            newList: {
              $map: {
                input: '$courses',
                as: 'course',
                in: {
                  $multiply: ['$$calificacion.progress', 10]
                }
              }
            }
        }
      }
  ]
)
