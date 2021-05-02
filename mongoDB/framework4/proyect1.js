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
      }
  ]
).pretty()
