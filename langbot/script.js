const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const chatLog = document.getElementById('chat-log');
const languageSelect = document.getElementById('language-select');

sendBtn.addEventListener('click', async () => {
    const userMessage = userInput.value.trim();
    const selectedLanguage = languageSelect.value;
    userInput.value = '';

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage, language: selectedLanguage }),
    });

    const data = await response.json();
    chatLog.innerHTML += `<p>You: ${userMessage}</p><p>LangBot: ${data.response}</p>`;
});