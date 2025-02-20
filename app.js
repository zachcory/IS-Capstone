// frontend/app.js
document.getElementById('messageForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const userId = document.getElementById('userId').value;
    const transactionId = document.getElementById('transactionId').value;
    const messageContent = document.getElementById('messageContent').value;

    fetch('/messages', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userId,
            transaction_id: transactionId,
            message_content: messageContent
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        loadMessages();
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('refreshMessages').addEventListener('click', function() {
    loadMessages();
});

function loadMessages() {
    fetch('/messages')
    .then(response => response.json())
    .then(messages => {
        const messageList = document.getElementById('messageList');
        messageList.innerHTML = '';
        messages.forEach(msg => {
            const li = document.createElement('li');
            li.textContent = `[${msg.received_at}] User ${msg.user_id}: ${msg.message_content}`;
            if (msg.is_duplicate) {
                li.classList.add('duplicate');
                li.textContent += ' (Duplicate)';
            }
            messageList.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error));
}

// Load messages when the page loads
window.onload = loadMessages;