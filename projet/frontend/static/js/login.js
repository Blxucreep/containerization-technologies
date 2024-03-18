document.addEventListener("DOMContentLoaded", function() {
    // check if the user is already logged in
    const accessToken = sessionStorage.getItem('accessToken');

    if (accessToken) {
        // redirect to the main page if the user is already logged in
        window.location.href = '/main';
    }
    
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
                // store the access token in the session storage
                response.json().then(data => {
                    console.log("data:", data);
                    sessionStorage.setItem('accessToken', data.access_token);
                    // redirect to the main page if the login is successful
                    window.location.href = '/main';
                });
            } else {
                // show an alert if the login failed
                alert('Username or password incorrect, please try again.');
            }
        })
        .catch(error => console.error('Error during login:', error));
    });
});
