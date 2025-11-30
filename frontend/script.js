const API_URL = "http://127.0.0.1:5000/chat";

const messagesDiv = document.getElementById("chat-messages");
const inputEl = document.getElementById("message-input");
const sendBtn = document.getElementById("send-button");

// Add a message bubble
function addMessage(text, sender) {
    const wrapper = document.createElement("div");
    wrapper.className = "message " + sender;

    const bubble = document.createElement("div");
    bubble.className = "message-content";
    bubble.textContent = text;

    wrapper.appendChild(bubble);
    messagesDiv.appendChild(wrapper);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Send message to backend
async function sendMessage() {
    const text = inputEl.value.trim();
    if (!text) return;

    addMessage(text, "user");
    inputEl.value = "";
    inputEl.focus();

    sendBtn.disabled = true;

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        });

        if (!res.ok) {
            addMessage("Server error (" + res.status + ").", "bot");
            return;
        }

        const data = await res.json();
        addMessage(data.reply || "No reply.", "bot");
    } catch (err) {
        addMessage("Cannot reach server. Is backend running?", "bot");
    } finally {
        sendBtn.disabled = false;
    }
}

// Events
sendBtn.addEventListener("click", sendMessage);
inputEl.addEventListener("keydown", e => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});
