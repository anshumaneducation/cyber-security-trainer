const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// List of allowed IPs
const allowedIPs = ["192.168.1.1", "127.0.0.1", "203.0.113.5"];

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// API to detect IP and send allowed status
app.get('/check-ip', (req, res) => {
    const clientIP = req.headers['x-forwarded-for'] || req.socket.remoteAddress;

    console.log("Client IP:", clientIP); // Log the detected IP for debugging

    // Check if the IP is in the allowed list
    const isAllowed = allowedIPs.includes(clientIP.replace('::ffff:', ''));
    res.json({
        success: isAllowed,
        message: isAllowed ? "Your IP is allowed. Welcome!" : "Your IP is not allowed. Access denied.",
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://192.168.201.245:${PORT}`);
});
