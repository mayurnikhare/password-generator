# 🔐 Password Manager Web App

A full-stack **Password Manager Web Application** built using Flask that allows users to securely generate, store, and manage passwords with a modern and responsive UI.

---

## 🚀 Features

* 🔑 User Authentication (Login/Register)
* 🔐 Secure Password Hashing
* 🎯 Custom Password Generator (length, uppercase, digits, symbols)
* 📊 Password History Dashboard (Last 5 passwords)
* 📋 Copy to Clipboard functionality
* 💪 Password Strength Indicator
* 🎨 Modern UI with Bootstrap + Glassmorphism + Gradient Effects

---

## 🛠️ Technologies Used

* Python
* Flask
* SQLite
* HTML, CSS
* Bootstrap
* JavaScript

---

## 📂 Project Structure

```
password-generator/
│
├── app.py
├── generator.py
├── database.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── register.html
│
└── static/
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

2. Install dependencies:

```
pip install flask flask-login werkzeug
```

3. Run the application:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Features

* Passwords are hashed using Werkzeug
* User-specific password storage
* Input validation for secure operations

---

## 🚀 Future Improvements

* 👁 Show/Hide password toggle
* 🗑 Delete saved passwords
* 🌐 Deploy online (Render / Railway)
* 🔒 Encrypt stored passwords

---

## 🌐 Live Demo

🔗 https://password-generator-b1qg.onrender.com

---

## 👨‍💻 Author

**Mayur Nikhare**

---

⭐ If you like this project, give it a star!
