const express = require('express');
let TasksController = require('../controllers/tasks');

let router = express.Router();

//ruta, grupo de pendientes, coleccion y crear coleccion, y peticion post
router.route('/tasks').get(TasksController.index).post(TasksController.create);
//function(req,res){  res.send('Hola mundo desde una subruta');}

router.get('/tasks/new',TasksController.new);       //consulta

router.get('/tasks/:id/edit',TasksController.edit);

router.route('/tasks/:id')
.get(TasksController.show)
.put(TasksController.update) //wildcard-comodin
.delete(TasksController.destroy);

module.exports = router;
