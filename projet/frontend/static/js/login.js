document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loginForm").addEventListener("submit", function(event) {
        event.preventDefault();
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        // do a fetch to the user-service to login the user
        fetch('http://localhost:5002/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => {
            if (response.ok) {
                // redirect to the main page if the login is successful
                window.location.href = '/main';
            } else {
                // show an alert if the login failed
                alert('Username or password incorrect, please try again.');
            }
        })
        .catch(error => console.error('Error during login:', error));
    });
});
