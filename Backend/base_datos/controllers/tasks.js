const Task = require('../models').Task;


module.exports = {
  home: function(req,res){
    Task.findAll().then(function(tasks){
      res.render('tasks/index',{tasks: tasks});
    });
  }
};
