db.createCollection( "contact",{
  validator: { $jsonSchema: {
    bsonType: "object",
    required: [ "phone" ],
    properties: {
      phone: {
        bsonType: "string",
        description: "must be a string and is required"
      },
      email: {
        bsonType : "string" ,
        pattern : "@mongodb\.com$" ,
        description: "must be a string an match the regular expression pattern"
      },
          status: {
          enum: [ "Unknow", "Incomplete" ],
          description: "can onlu be one of the enum values"
      }
    }
  } }
} )

//
var contacto = {
  phone: '0000-00',
  email: 'mytacam78@gmail.com',
  status : 'Victor'
}

db.contacts.insertOne(contacto)
