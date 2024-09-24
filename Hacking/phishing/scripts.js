document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Simulate capturing user data (for training purposes only)
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Display a fake phishing warning message
    alert('This was a phishing simulation.\n\nYour email: ' + email + '\nYour password: ' + password + '\n\nRemember: Never enter your credentials on a suspicious site!');
    
});
