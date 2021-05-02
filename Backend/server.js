const http = require('http');

function responderPeticion(request, response) {
    response.end('madre, ya sé programar');
}

let server = http.createServer(responderPeticion);

server.listen(3000);