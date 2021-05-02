db.users.updateOne(
  {
    name: 'Fernando'
  },
  {
    $set: {
      'courses.0.progress': 100,
      'courses.0.completed': true,
    }
  }
)

// 2.1
db.users.updateOne(
  {
    name: 'Pablo',
    'courses.title': 'MongoDB'
  },
  {
    $set: {
      'courses.0.progress': 100,
      'courses.0.completed': true,
      'courses.$.tutor': {
        'name': 'Cody'
      }
    }
  }
)

///3
db.users.updateOne(
  {
    name: 'Pablo',
    'courses.title': 'MongoDB'
  },
  {
    $set: {
      'courses.$.tutor.name': 'CodigoFacilito'
    }
  }
)
