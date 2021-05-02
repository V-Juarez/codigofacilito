const { ApolloServer } = require('apollo-server');
const { makeExecutableSchema } = require('graphql-tools');

const courses = require('./courses');

const typeDefs = `
        id: ID!
        title: String!
        views: Int
    }

    type Alert{
     message: String   
    }

    input CourseInput{
        title: String!
        views: Int  
    }

    type Query {
        getCourses(page: Int, limit: Int = 1): [Course]
        getCourse(id: ID!): Course
    }

    type Mutation {
        addCourse(input: CourseInput): Course
        updateCourse(id: ID!, input: CourseInput): Course
        deleteCourse(id: ID!):Alert
    }
`;

const resolvers = {
     Query: {
         getCourses(obj, { page, limit }) {
            if (page !== undefined) {
                return courses.slice((page - 1) * limit, (page) * limit);
            }
            return courses;
        },
        getCourses(obj,{ id }) {
            console.log(id);
            return courses.find((course) => id == course.id);
        }
        },
         Mutation: {
            addCourse(obj,{ input }){
                const id = String(courses.length + 1);
                const course = { id, ...input }; //spread operator
                courses.push(course);
                return course;
            },
            updateCourse(obj,{ id, input }) {
                const courseIndex = courses.findIndex((course) => id === course.id );
                const course = courses[courseIndex];

                const newCourse = Object.assign(course, input);
                course[courseIndex] = newwCourse;

                return newCourse;
        },
            deleteCourse(obj,{id}){
                courses = courses.filter((course) => course.id != id);
                return{
                message: `El curso con id ${id} fue eliminado`
           }
        }
        
    }     
}

const schema = makeExecutableSchema({
    typeDefs,
    resolvers
})

const server = new ApolloServer({
    schema: schema
});

server.listen().then(({url}) => {
    console.log(`Servidor iniciado en ${url}`);
});