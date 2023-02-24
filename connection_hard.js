function process() {
    const WebSocket = require('ws');
    const ws = new WebSocket("ws://localhost:8080");
    ws.addEventListener("", () =>{
    console.log("We are connected");
    });
    
    ws.addEventListener('message', function (event) {
        console.log(event.data);
    });

    function sendRequestLogin() {
        ws.send(`
            username: admin
            password: Lehigh123
        `);
    }

    function sendRequestHtml() {
    ws.send("html");
    }

    function sendRequestPing() {
    ws.send("Ping");
    }

    function sendRequestPassword() {
        ws.send("Password");
    }

    setTimeout(sendRequestLogin, 1000);
    setInterval(sendRequestPing, 1000);
    setInterval(sendRequestHtml, 2000);
    // pause here
    setTimeout(() => {ws.close()},6000)
}

process()
setInterval(process, 20000);
