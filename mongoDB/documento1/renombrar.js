db.users.updateMany(
  {},
  {
    $rename: {
      last_name:'lastName'
    }
  }
)
