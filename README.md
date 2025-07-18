
# 🔥 Real-Time Text Stream with Flask + Redis + SSE

Simple real-time broadcasting app using **Flask**, **Redis Pub/Sub**, and **Server-Sent Events (SSE)**.  
Perfect for announcements, logs, messages, and live text updates—no WebSocket needed.

---

## 🧠 How It Works

1. `publisher.py` pushes messages to Redis on `main_channel`.
2. Flask server listens to Redis and streams messages via `/text-content`.
3. Frontend (`index.html`) auto-updates the UI with each new message received via SSE.

---

## 🚀 Quickstart

### 📦 Install Dependencies

```bash
pip install flask redis
````

Make sure Redis is installed and running on `localhost:6379`.

### 📡 Run the Flask Server

```bash
python app.py
```

### 💬 Start Publishing Messages

```bash
python publisher.py
```

Type any message and hit enter to broadcast it.

---

## 🌐 Frontend (SSE Client)

Located in `templates/index.html`

* Connects to `/text-content`
* Listens for incoming messages
* Auto-appends them to the DOM in real-time

---

## ✅ Features

* Real-time UI updates using SSE
* Clean pub/sub flow using Redis
* Auto-reconnect handled by browser
* Thread-safe streaming with `stream_with_context`
* Minimal boilerplate, fully extendable

---

## 🧪 Test Message

Once server and publisher are running:

```bash
Enter message to broadcast: Hello world 👋
```

Will instantly appear on the frontend as:

```
🗣️ Hello world 👋
```

---

## 🛠️ Customization Ideas

* Add authentication before allowing access to `/text-content`
* Broadcast from other services/scripts
* Push system logs or status updates
* Style frontend with animations or timestamps

---

📄 **Original Version (Without Redis)**  
Want the simpler version without Redis?  
👉 Check the [`simple-sse` branch](https://github.com/jztchl/sse_demo/tree/main)
