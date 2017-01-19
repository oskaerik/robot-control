// Set up input server
var inputServer = require('express')();
var inputHttp = require('http').Server(inputServer);
var io = require('socket.io')(inputHttp);
var lastInput = "no";

inputServer.get('/', function(request, response) {
  response.sendFile(__dirname + '/index.html');
})

// When a user connects
io.on('connection', function(socket) {
  console.log("User connected");

  // If a client event is recieved
  socket.on('touching', function(data) {
    console.log(data);
    lastInput = data;
  })

  // When the user disconnects
  socket.on('disconnect', function() {
    console.log("User disconnected")
  });
});


// Set up output server
var outputServer = require('express')();
var outputHttp = require('http').Server(outputServer);

outputServer.get('/', function(request, response) {
  response.write(lastInput);
  response.end();
})


// Run servers
var inputPort = 3000;
inputHttp.listen(inputPort, function() {
  console.log("Input server running on port " + inputPort)
});

var outputPort = 3001;
outputHttp.listen(outputPort, function() {
  console.log("Output server running on port " + outputPort)
});
