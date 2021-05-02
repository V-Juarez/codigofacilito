mongodump         realizar respaldo de la base de datos

mongodump --db cursoMongoDB
mongodump --collections users --db cursoMongoDB

mongorestore     -> restablece la base de datos
mongorestore --db cursoMongoDB dump/cursoMongoDB

mongorestore --collection users --db cursoMongoDB dump/cursoMongoDB/users.bson
