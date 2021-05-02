const express = require('express');
const { GraphQLSchema, GraphQLObjectType, GraphQLString, graphql, GraphQLInt } = require('graphql');

const app = express();

const courseType = new GraphQLObjectType({
  name: 'Course',
  fields:{
    title: { type: GraphQLString },
    views: { type: GraphQLInt }
  }
});

const schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: "RootQueryType",
    fields:{
      message : {
        type: GraphQLString,
        resolve(){
          return "hola Mundo";
        }
      },
      course:{
        type: courseType,
        resolve(){
          return{ title: 'Curso de GraphQL', views: 1000 };
        }
      }
    }
  })
});

app.get('/',function(req,res){
  graphql(schema,` { message, course{ title, views } } `).then(r => res.json(r)).catch(res.json);
});

app.listen(8080,function(){
  console.log("Servidor iniciado");
})
