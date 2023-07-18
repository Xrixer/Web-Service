const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server, {cors:{ origin: "*"}});
const puerto = 3000;

class Partida {
    constructor(jwt,jugadores,ordenTurno,turno) {
        this.jwt = jwt;
        this.jugadores = [];
        this.ordenTurno = [];
        this.turno = turno;
    }

    agregarJugador(username, socketId) {
        this.jugadores.push(new Jugador(username, socketId));
    }
}

class Jugador {
    constructor(username, socketId, turno) {
        this.username = username;
        this.socketId = socketId;
        this.turno = turno
    }
}

// var jugadoresPermitidos = ["Gabriel", "JoseEnrique", "J", "Hernan"];
// http://localhost:3000/?username=Gabriel
// http://localhost:3000/?username=Jose Enrique
// http://localhost:3000/?username=J
// http://localhost:3000/?username=Hernan

// var jugadoresPermitidosCheck = [0, 0, 0, 0];
// const piezasRepartidas = [];  // matriz con las piezas repartidas
// piezasRepartidas[0] = [];      // Piezas del jugador 0
// piezasRepartidas[1] = [];      // Piezas del jugador 1
// piezasRepartidas[2] = [];      // Piezas del jugador 2, el compañero
// piezasRepartidas[3] = [];      // Piezas del jugador 3


var partidas = []


app.get('/', (req, res) => {

    const found = partidas.find(partida => partida.jwt === req.query.token)
    if(!found){
        const partida = new Partida(req.query.token);
        partidas.push(partida);
    }

    res.sendFile(__dirname + '/DominoCliente.html');

    // var contJugadores = 0;
    // var encontrado = false;
    // for(var i =0 ; i<4 ; i++){
    //     if(jugadoresPermitidos[i] == req.query.username){
    //         jugadoresPermitidosCheck[i]=1;
    //         encontrado = true;
    //         console.log(req.query.username + " se ha conectado");
    //         res.sendFile(__dirname + '/clientico.html');
    //     }
    //     contJugadores+=jugadoresPermitidosCheck[i];
    // }

    // if(!encontrado)
    //     res.sendFile(__dirname + '/error.html');
    // console.log(contJugadores + " jugadores conectado(s)");
    // if(contJugadores == 4) // listo, todos conectados
    //     ComenzarJuego();
    

});

io.on('connection', (socket) => {
    console.log();

    socket.on("message", (data) => {
        console.log(" Hola "+ data);
        var contJugadores = 0;
        
    });

    socket.on("make.move", (arg)=>{
        // let jugador = find(jugador);
        // partida.jugarPieza(jugador,pieza);
        // //partida con el estado de las piezas
        //broadcast actualiza a todos los demas jugadores 
        io.emit("made.move", data);
    });

    socket.on("connect-player", (data) => {
        // send a message to the server

        const partida = partidas.find(partida => partida.jwt == data.token)

        if(partida){
            const user = new Jugador(data.username, socket.id);
            partida.agregarJugador(user);
            socket.emit("numero-jugador", partida.jugadores.length);

            if(partida.jugadores.length == 4){
                RepartirPiezas(partida);
                io.emit("start-game",{partida});
            }
        }

        });
    });

    server.listen(puerto, () => {
  console.log('listening on *'+puerto);
});

// Funciones del Juego Domino

class PiezaNN{
    constructor(nombre, pos){
        this.nombre = nombre;
        this.pos = pos;
    }
}

function RepartirPiezas(partida) {

    const jugadores = partida.jugadores;
    var piezasN = []
    
    var contPiezas = 0;
    for (let i = 0; i < 7; i++) // Las crea
        for (let j = i; j < 7; j++) {
            var nombre = i.toString()+j.toString();
            var pieza = new PiezaNN(nombre, contPiezas++);
            piezasN.push(pieza);
        }
    for(let i = 0; i < jugadores.length; i++)  // Las reparte
        for(let j = 0; j < 7; j++){
            var np = Math.floor(Math.random() * piezasN.length);
            jugadores[i].piezas.push(piezasN[np]);
            jugadores[i].turno = i;
            if(piezasN[np].nombre == "66")
                partida.turno = i; // jugador que inicia la partida (Cochina)
            piezasN.splice(np, 1); // Elimina la piezas repartida
        }          
}
