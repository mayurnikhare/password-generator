from flask import Flask, render_template, request, redirect, url_for
import sqlite3

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from generator import generate_password

app = Flask(__name__)
app.secret_key = "secret123"

# ================= LOGIN =================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ================= DATABASE =================
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ================= USER =================
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

# ================= LOAD USER =================
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return User(user[0], user[1])
    return None

# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return redirect(url_for("login"))
        except:
            return "User already exists!"

    return render_template("register.html")

# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            login_user(User(user[0], user[1]))
            return redirect(url_for("index"))

        return "Invalid credentials!"

    return render_template("login.html")

# ================= LOGOUT =================
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# ================= MAIN =================
@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    password = ""

    if request.method == "POST":
        length = int(request.form.get("length"))

        if length <= 0:
            return "Length must be greater than 0"

        use_upper = "upper" in request.form
        use_digits = "digits" in request.form
        use_symbols = "symbols" in request.form

        password = generate_password(length, use_upper, use_digits, use_symbols)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO passwords (user_id, password) VALUES (?, ?)",
            (current_user.id, password)
        )
        conn.commit()
        conn.close()

    # 🔥 FETCH HISTORY
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
SELECT password FROM passwords 
WHERE user_id=? 
ORDER BY id DESC 
LIMIT 5
""", (current_user.id,))
    history = cursor.fetchall()
    conn.close()

    return render_template("index.html", password=password, history=history)

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)