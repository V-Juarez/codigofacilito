const express = require('expess');
const app = express();

app.get("/",(req,res)=>{
  res.send("hola mundo");
})

app.listen(3000,()=> console.log("server started"));
