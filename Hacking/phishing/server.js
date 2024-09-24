const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

// Broadcast function to send data to all connected clients
function broadcast(data) {
    wss.clients.forEach(function each(client) {
        if (client.readyState === WebSocket.OPEN) {
            client.send(data);
        }
    });
}

wss.on('connection', function connection(ws) {
    console.log('Client connected');

    // Listen for messages from clients
    ws.on('message', function incoming(data) {
        // Ensure data is treated as a string and parsed if necessary
        const message = data.toString(); // Convert buffer to string
        
        console.log('Received data from client:', message);

        try {
            const jsonData = JSON.parse(message); // Parse the JSON string if needed

            // Re-stringify the JSON data to broadcast it
            const broadcastData = JSON.stringify(jsonData);

            // Broadcast the received data to all connected clients
            broadcast(broadcastData);
        } catch (e) {
            console.error('Error parsing JSON data:', e);
        }
    });

    ws.on('close', function() {
        console.log('Client disconnected');
    });
});

console.log('WebSocket server is running on ws://localhost:8080');
