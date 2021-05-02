'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {

      return queryInterface.bulkInsert('tasks', [
      {id: 1, description: 'Grabar el curso de Backend',createdAt: new Date(), updatedAt: new Date()},
      {id: 2, description: 'Editar los videos del curso de Backend',createdAt: new Date(), updatedAt: new Date()},
      {id: 3, description: 'Subir los videos',createdAt: new Date(), updatedAt: new Date()},
      {id: 4, description: 'Curso Backend',createdAt: new Date(), updatedAt: new Date()}
    ], {});

  },

  down: (queryInterface, Sequelize) => {

      return queryInterface.bulkDelete('tasks', null, {});
  }
};
