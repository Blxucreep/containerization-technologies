// Exemple d'initialisation de la gestion des salles de chat et de la soumission des messages
document.addEventListener('DOMContentLoaded', function() {
    // Gestion de la création de nouvelles salles de chat
    const createRoomButton = document.querySelector('.create-room-btn');
    if (createRoomButton) {
        createRoomButton.addEventListener('click', function() {
            const roomName = prompt("Enter the name of the room:");
            if (roomName) {
                console.log("Create room:", roomName);
                // Ici, vous ajouterez la logique pour créer une salle de chat côté serveur
            }
        });
    }

    // Gestion de l'envoi de messages dans une salle de chat
    const messageForm = document.getElementById('messageInputForm');
    if (messageForm) {
        messageForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const messageInput = document.getElementById('messageInput');
            const message = messageInput.value.trim();
            if (message) {
                console.log("Message to send:", message);
                // Ici, vous ajouterez la logique pour envoyer le message au serveur
                messageInput.value = ''; // Réinitialiser l'input après envoi
            }
        });
    }
});

// Vous pouvez également ajouter des gestionnaires d'événements pour la recherche d'utilisateurs si nécessaire.
