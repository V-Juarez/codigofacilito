const express = require('express');

let ResgistrationsController = require('../controllers/registrations');
let router = express.Router();


router.get('/signup',ResgistrationsController.new);

router.route('/users').post(ResgistrationsController.create);

module.exports = router;
