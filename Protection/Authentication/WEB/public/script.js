document.getElementById('ip-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const ip = document.getElementById('ip-input').value.trim();
    const responseMessage = document.getElementById('response-message');

    // Send IP to the server for validation
    const response = await fetch('/validate-ip', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ip }),
    });

    const data = await response.json();

    // Display the server's response
    responseMessage.textContent = data.message;
    responseMessage.style.color = data.success ? 'green' : 'red';
});
