document.addEventListener("DOMContentLoaded", function() {
    // retrieve the username from the session storage
    const storedUsername = sessionStorage.getItem('username');

    if (!storedUsername) {
        // display a warning message and redirect to the login page
        alert('You need to be logged in to access this page!');
        window.location.href = '/login';
    }

    // update the links in the navigation bar
    if (storedUsername) {
        // update the welcome message in the navigation bar
        const welcomeMessage = document.querySelector("nav a:first-child");
        if (welcomeMessage) {
            welcomeMessage.textContent = `Welcome, ${storedUsername}!`;
        }
        // update the login link in the navigation bar
        const loginLink = document.querySelector("nav a[href='/login']");
        if (loginLink) {
            loginLink.style.display = "none";
        }
        
        // update the register link in the navigation bar
        const registerLink = document.querySelector("nav a[href='/register']");
        if (registerLink) {
            registerLink.style.display = "none";
        }
    }
    else {
        // update the welcome message in the navigation bar
        const welcomeMessage = document.querySelector("nav a:first-child");
        if (welcomeMessage) {
            welcomeMessage.style.display = "none";
        }

        // update the logout link in the navigation bar
        const logoutLink = document.querySelector("nav a[href='/logout']");
        if (logoutLink) {
            logoutLink.style.display = "none";
        }
    }

    // function to fill the user list
    function fillUserList() {
        fetch('http://localhost:5002/get_users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById("userList");
            userList.innerHTML = "";
            data.users.forEach(user => {
                // don't show the current user in the list
                if (user.username !== sessionStorage.getItem('username')) {
                    const listItem = document.createElement("li");
                    listItem.textContent = user.username;
                    listItem.addEventListener("click", function() {
                        displayMessages(user);
                    });
                    userList.appendChild(listItem);
                }
            });
        })
        .catch(error => console.error('Error:', error));
    }

    // function to display the messages for the selected user
    function displayMessages(user, onlyUsername = false) {
        username = user.username;
        if (onlyUsername) {
            username = user; // if the user is a string, it's the username
        }
        fetch(`http://localhost:5001/get_messages/${username}`)
        .then(response => response.json())
        .then(data => {
            // display the username to which the messages belong
            const toWhoIAmTalking = document.getElementById("your-messages");
            toWhoIAmTalking.textContent = `Your messages with ${username}`;
            toWhoIAmTalking.name = username;
            console.log("username:", username);
            console.log("data:", data);

            // display the messages
            const messagesDiv = document.getElementById("messages");
            messagesDiv.innerHTML = "";
            data.messages.forEach(message => {
                const messageDiv = document.createElement("div");
                messageDiv.textContent = `${message.sender}: ${message.content}`;
                messagesDiv.appendChild(messageDiv);
            });
        })
        .catch(error => console.error('Error:', error));
    }

    // then display the messages for the first user in the list (if there is one)
    const firstUser = document.querySelector("#userList li");
    if (firstUser) {
        displayMessages(firstUser.textContent);
    }

    // event to send a message
    document.getElementById("messageInputForm").addEventListener("submit", function(event) {
        event.preventDefault();
        const messageInput = document.getElementById("messageInput").value;
        const selectedUser = document.getElementById("your-messages").name;
        if (!selectedUser) {
            alert("Please select a user to send a message to.");
            return;
        }
        const data = {
            sender: sessionStorage.getItem('username'),
            receiver: selectedUser,
            content: messageInput
        };
        fetch("http://localhost:5001/send_message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                // refresh the messages for the selected user
                displayMessages(selectedUser, true);
                document.getElementById("messageInput").value = "";
            } else {
                alert("Error sending message, please try again.");
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // event to logout the user
    document.getElementById("logout").addEventListener("click", function() {
        sessionStorage.removeItem('username');
        window.location.href = '/login';
    });

    // call the function to fill the user list
    fillUserList();
});
