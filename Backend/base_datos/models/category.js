'use strict';
module.exports = (sequelize, DataTypes) => {
  const Category = sequelize.define('Category', {
    title: DataTypes.STRING,
    color: DataTypes.STRING
  }, {});
  Category.associate = function(models) {// associations can be defined here
    Task.belongsToMany(models.Task,{
      through: 'TaskCategories',
      as: 'tasks'
    });
  };
  return Category;
};
