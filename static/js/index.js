let chat = document.querySelector('#chat');
let input = document.querySelector('#input');
let sendButton = document.querySelector('#send-button');

async function sendMessage() {
    if (input.value == "" || input.value == null) return;
    let message = input.value;
    input.value = "";

    let newUserBubble = createUserBubble();
    newUserBubble.innerHTML = message;
    chat.appendChild(newUserBubble);

    let newBotBubble = createBotBubble();
    chat.appendChild(newBotBubble);
    scrollToChatEnd();
    newBotBubble.innerHTML = "Analyzing...";

    // Sends the request with the message to the ChatBot API
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'msg': message }),
    });
    const responseText = await response.text();
    console.log(responseText);
    newBotBubble.innerHTML = responseText.replace(/\n/g, '<br>');
    scrollToChatEnd();
}

function createUserBubble() {
    let bubble = document.createElement('p');
    bubble.classList = 'chat__bubble chat__bubble--user';
    return bubble;
}

function createBotBubble() {
    let bubble = document.createElement('p');
    bubble.classList = 'chat__bubble chat__bubble--bot';
    return bubble;
}

function scrollToChatEnd() {
    chat.scrollTop = chat.scrollHeight;
}

sendButton.addEventListener('click', sendMessage);
input.addEventListener("keyup", function (event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        sendButton.click();
    }
});

function clearConversation() {
    fetch("http://127.0.0.1:5000/clearhistory", {
        method: "POST"
    });
    chat.innerHTML = "<p class='chat__bubble chat__bubble--bot'>Hello! I am the virtual assistant of Sabor Express ~<br/><br/>How can I help you?</p>";
}
