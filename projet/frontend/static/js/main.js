document.addEventListener("DOMContentLoaded", function() {
    // function to fill the user list
    function fillUserList() {
        fetch('http://localhost:5002/get_users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById("userList");
            userList.innerHTML = "";
            data.users.forEach(user => {
                // don't show the current user in the list
                if (user !== "{{ username }}") {
                    const listItem = document.createElement("li");
                    listItem.textContent = user;
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
    function displayMessages(username) {
        fetch(`http://localhost:5001/get_messages/${username}`)
        .then(response => response.json())
        .then(data => {
            const messagesDiv = document.getElementById("messages");
            messagesDiv.innerHTML = "";
            data.received_messages.forEach(message => {
                const messageDiv = document.createElement("div");
                messageDiv.textContent = `${message.sender_id}: ${message.content}`;
                messagesDiv.appendChild(messageDiv);
            });
        })
        .catch(error => console.error('Error:', error));
    }

    // event to send a message
    document.getElementById("messageInputForm").addEventListener("submit", function(event) {
        event.preventDefault();
        const messageInput = document.getElementById("messageInput").value;
        const selectedUser = document.querySelector("#userList li.active");
        if (!selectedUser) {
            alert("Please select a user to send a message to.");
            return;
        }
        const recipient = selectedUser.textContent;
        const data = {
            sender_id: "{{ username }}", // current user
            receiver_id: recipient,
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
                displayMessages(recipient);
                document.getElementById("messageInput").value = "";
            } else {
                alert("Error sending message, please try again.");
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // call the function to fill the user list
    fillUserList();
});
