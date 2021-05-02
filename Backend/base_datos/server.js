const express = require('express');
const sqlite3 = require('sqlite3');
const bodyParser = require('body-parser');
const Sequelize = require('Sequelize');


const app  = express();

const tasks = require('./controllers/tasks');

app.use(bodyParser.urlencoded({extended: true}));

/*const sequelize = new Sequelize('proyecto-backend',null,null,{  //ingresar al servidor, se recomienda ingresar solo una vez al servidor.
  dialect: 'sqlite',
  storage: './proyecto-backend'
});*/
//let db = new sqlite3.Database('proyecto-backend');

app.set('view engine','pug');

app.get('/tasks',tasks.home);

app.post('/pendientes',function(req,res){
  //db.run(`INSERT INTO tasks(description) VALUES(?)`,req.body.description);
  res.send('Inserción finalizada');
});



//db.run('CREATE TABLE tasks(id int AUTO_INCREMENT, description varchar(255))');

app.listen(3000);

/*process.on('SIGINT',function(){               //conectarse al servidor y lugo al terminar de porcesar los datos la coneccion se a de cerrar
  console.log('bye - Atte. El servidor');
  db.close();
  process.exit();
});*/
