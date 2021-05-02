const express = require('express');
const mongoose = rerquire('mongoose');

mongoose.conect('mongobd://localhost/graphql_Base-Datos_course')

const app = express();

app.listen(8000,function){
    console.log("servidor inciando");
})