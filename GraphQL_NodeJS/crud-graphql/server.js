const express = require('express');
const {buildSchema} = require('graphql');
const graphqlHTTP = require('express-graphql');

const courses = require('./courses');

const app = express();

//schema definition language
const schema = buildSchema(`
  type Course{
    id: ID!
    title: String!
    views: Int
  }

  type Query {
    getCourses: [Course]
    getCourse(id: ID!): Course
  }

  type Mutation {
    addCourse(title: String!, views: Int): Course
    updateCourse(id: ID! title: String!, views: Int): Course
  }
  `); //Template strings

const root = {
  getCourses(){
    return courses;
  },
  getCourse( { id } ){
    console.log(id);
    return courses.find( (course)=> id == course.id );
  },
  addCourse({title, views}){
    const id = String(course.length + 1);
    const course = { id, title, views };
    courses.push(course);
    return course;
  },
  updateCourse({id, title, views}){
    const courseIndex = courses.findIndex((course)=> id == course.id );
    const course = courses[courseIndex];

    const newCourse = Object.assign(course,{ title, views });
    const[courseIndex] = newCourse;

    return newCourse;
  }
}

app.get('/',function(req,res){
  res.json(courses);
});

//middleware
app.use('/graphql',graphqlHTTP({
  schema,
  rootValue: root,
  graphql: true
}));

app.listen(8080,function(){
  console.log("Servidor iniciado");
});
