document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    
    if (userInput.trim() !== '') {
        // Display user message
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user');
        userMessage.innerHTML = `<div class="avatar">U</div><div class="content">${userInput}</div>`;
        chatBox.appendChild(userMessage);
        
        // Scroll to the bottom
        chatBox.scrollTop = chatBox.scrollHeight;
        
        // Send message to the backend
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `message=${userInput}`
        })
        .then(response => response.json())
        .then(data => {
            // Display bot response
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.innerHTML = `<div class="avatar">B</div><div class="content">${data.response}</div>`;
            chatBox.appendChild(botMessage);
            
            // Scroll to the bottom
            chatBox.scrollTop = chatBox.scrollHeight;
        });
        
        // Clear input
        document.getElementById('user-input').value = '';
    }
});

