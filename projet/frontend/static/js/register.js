document.addEventListener("DOMContentLoaded", function() {
    // check if the user is already logged in
    const accessToken = sessionStorage.getItem('accessToken');

    if (accessToken) {
        // redirect to the main page if the user is already logged in
        window.location.href = '/main';
    }
    
    document.getElementById("registrationForm").addEventListener("submit", function(event) {
        event.preventDefault();
        let username = document.getElementById("username").value;
        let password = document.getElementById("password").value;

        // do a fetch to the user-service to register the user
        fetch('http://localhost:5002/signup', {
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
                // redirect to the login page if the registration is successful
                window.location.href = '/login';
            } else {
                // show an alert if the registration failed
                alert('Error during registration, please try again.');
            }
        })
        .catch(error => console.error('Error during registration:', error));
    });
});
