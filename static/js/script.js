var username = prompt("Please enter your username");
var usernameDisplay = document.getElementById("usernameDisplay");
usernameDisplay.textContent = "Username: " + username;
var messageInput = document.getElementById("messageInput");
var messages = document.getElementById("messages");
var chatroom = window.location.pathname.split("/")[1];
var ws = new WebSocket(`ws://localhost:8000/ws/${chatroom}/${username}`);
console.log(chatroom);

ws.onmessage = function (event) {
  var message = document.createElement("div");
  message.textContent = event.data;
  message.classList.add("message");

  if (event.data.includes("joined the chat")) {
    message.classList.add("join");
  } else if (event.data.includes("left the chat")) {
    message.classList.add("left");
  } else if (event.data.startsWith("You:")) {
    message.classList.add("own");
  } else {
    message.classList.add("other");
  }

  messages.appendChild(message);
};

function sendMessage() {
  ws.send(messageInput.value);
  messageInput.value = "";
}
