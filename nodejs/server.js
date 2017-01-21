// Set up input server
var inputServer = require('express')();
var inputHttp = require('http').Server(inputServer);
var inputIO = require('socket.io')(inputHttp);
var inputSocket = null;

// Movement array, 0: up, 1: down, 2: right, 3: left
var movement = [false, false, false, false];

inputServer.get('/', function(request, response) {
  response.sendFile(__dirname + '/index.html');
})

// When a user connects
inputIO.on('connection', function(socket) {
  console.log("User connected to input server");
  inputSocket = socket;

  // If a client event is recieved
  socket.on('touch', function(index, state) {
    movement[index] = state;
    console.log(movement);
    if (outputSocket) {
      outputSocket.emit('event', movement);
    }
  });

  // When the user disconnects
  socket.on('disconnect', function() {
    console.log("User disconnected from input server");
    if (socket == inputSocket) {
      inputSocket = null;
      movement = [false, false, false, false];
      if (outputSocket) {
        outputSocket.emit('event', movement);
      }
    }
  });
});


// Set up output server
var outputServer = require('express')();
var outputHttp = require('http').Server(outputServer);
var outputIO = require('socket.io')(outputHttp);
var outputSocket = null;

// When a user connects
outputIO.on('connection', function(socket) {
  console.log("User connected to output server");
  outputSocket = socket;

  // When the user disconnects
  socket.on('disconnect', function() {
    console.log("User disconnected from output server");
    if (socket == outputSocket) {
      outputSocket = null;
    }
  });
});

// Run servers
var inputPort = 3000;
inputHttp.listen(inputPort, function() {
  console.log("Input server running on port " + inputPort);
});

var outputPort = 3001;
outputHttp.listen(outputPort, function() {
  console.log("Output server running on port " + outputPort);
});
