# JustUpload 🚀  
A lightweight static website hosting platform inspired by Netlify & Vercel.

JustUpload allows developers to deploy HTML, CSS, and JavaScript websites instantly with **zero configuration**. Upload your files, and your site is live within seconds.

---

## ✨ Features

- 📁 Upload static websites (HTML, CSS, JS)
- ⚡ Instant deployment with live preview URLs
- 🖱️ Drag & drop file upload support
- 🌐 Auto-hosted static files using FastAPI
- 🔒 Secure by design (static files only)
- ♻️ Easy redeploy by re-uploading files
- 📱 Responsive UI (mobile + desktop)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Hosting:** FastAPI StaticFiles
- **Tools:** Uvicorn, Git

---

## 📁 Project Structure

```text
JustUpload/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── sites/            # Hosted websites (runtime)
├── frontend/
│   └── index.html
├── .gitignore
└── README.md



