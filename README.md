
---

# ⚡ Flask SSE Demo

Simple Flask app streaming real-time data via **Server-Sent Events**.

## 🔥 Features

* Live timestamp (`/text-content`)
* Live random JSON (`/json-content`)
* Auto-updating frontend with vanilla JS

## 🚀 Run

```bash
pip install flask
python app.py
```

Open `http://localhost:5000/`

---

📄 **Simple Version (Without Redis)**  
Want the scalable version with Redis?  
👉 Check the [`redis-sse` branch](https://github.com/jztchl/sse_demo/tree/scalable_version)