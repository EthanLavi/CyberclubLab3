// Importing the required modules
const WebSocketServer = require('ws');
 
// Creating a new websocket server
const wss = new WebSocketServer.Server({ port: 8080 })
 
// Creating connection using websocket

wss.on("connection", ws => { 
    console.log("new client connected");   
    
    // sending message to client
    // ws.send('Welcome, you are connected!'); //send back a lot of staff
    // ws.send("User authenticated, ", ws.data)
 
    //on message from client
    ws.on("message", data => {
        // console.log(`Client has sent us: ${data}`)
        console.log(data)

        let login = `
        username: admin
        password: Lehigh123
      `

        if (data == login) { 
            ws.send("User authenticated, ", ws.data)
        }

        if (data == "Hello") {
          ws.send("Hey!"); //send a lot of stuff here
        }

        if (data == "html") {
            let htmlPage = `
            <!DOCTYPE html>
            <html>
            <head>
            <title>Page Title</title>
            </head>
            <body>
            <p>This is a paragraph.</p>
            </body>
            </html>
        `
            ws.send(htmlPage)
        }

        if (data == "Ping") {
            ws.send("Pong")
        }
    });
 
    // handling what to do when clients disconnects from server
    ws.on("close", () => {
        console.log("the client has disconnected");
    });
    // handling client connection error
    ws.onerror = function () {
        console.log("Some Error occurred")
    }
});




console.log("The WebSocket server is running on port 8080");