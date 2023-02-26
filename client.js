const WebSocket = require('ws');

function process() {
	try {
		const ws = new WebSocket("ws://10.9.0.6:8080");
		ws.onerror = function(event){
			//console.log("Error");
		}

		ws.addEventListener("", () =>{
			//console.log("We are connected");
		});
    
		ws.addEventListener('message', function (event) {
			//console.log(event.data);
		});

		function sendRequestLogin() {
			ws.send(`username:admin|password:Lehigh123`);
		}

		function sendRequestHtml() {
			ws.send("html");
		}

		function sendRequestPing() {
			ws.send("Ping");
		}

		setTimeout(sendRequestLogin, 1000);
		setTimeout(() => {setInterval(sendRequestPing, 500)}, 2000);
		setTimeout(() => {setInterval(sendRequestHtml, 1000)}, 2000);
		// pause here
		setTimeout(() => {ws.close()}, 12000)
	} catch(err){
		return;
	}
}

console.log("Starting client emulation...")

setTimeout(process, 3000);
setInterval(process, 20000);


