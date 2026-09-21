import sqlite3
import string
import secrets
from urllib.parse import urlparse
from flask import Flask, request, jsonify, redirect, g

app = Flask(__name__)
DATABASE = "urls.db"

# ---------------------------------------------------------
# 1. DATABASE SETUP
# ---------------------------------------------------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute("CREATE TABLE IF NOT EXISTS urls ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "code TEXT UNIQUE NOT NULL, "
                 "original_url TEXT NOT NULL, "
                 "clicks INTEGER NOT NULL DEFAULT 0, "
                 "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    conn.close()

# ---------------------------------------------------------
# 2. RANDOM SHORT CODE
# ---------------------------------------------------------
def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    conn = get_db()
    while True:
        code = ''.join(secrets.choice(characters)
                       for _ in range(length)
                       )
        existing = conn.execute("SELECT id FROM urls WHERE code = ?",
                                (code,)
                                ).fetchone()
        if existing is None:
            return code

# ---------------------------------------------------------
# 3. VALIDATE URL
# ---------------------------------------------------------
def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return  parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False

# ---------------------------------------------------------
# 4. CREATE SHORT URL
# ---------------------------------------------------------
@app.post("/shorten")
def shorten_url():
    data = request.get_json()
    if not data:
        return jsonify({
            "error": "Request body must be JSON"
        }), 400

    original_url = data.get("url")
    if not original_url:
        return  jsonify({
            "error": "URL is required"
        }), 400

    if not is_valid_url(original_url):
        return jsonify({
            "error": "Invalid URL"
        }), 400

    conn = get_db()
    code = generate_code()
    conn.execute("INSERT INTO urls(code, original_url) "
                 "VALUES (?, ?)",
                 (code, original_url)
                 )
    conn.commit()

    short_url = request.host_url + code

    return jsonify({
        "code": code,
        "original_url": original_url,
        "short_url" : short_url
    }), 201

# ---------------------------------------------------------
# 5. REDIRECT
# ---------------------------------------------------------
@app.get("/<code>")
def redirect_url(code):
    conn = get_db()
    row = conn.execute("SELECT * FROM urls WHERE code = ?",
                       (code,)
                       ).fetchone()

    if row is None:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    conn.execute("UPDATE urls "
                 "SET clicks = clicks + 1 "
                 "WHERE code = ?", (code,)
                 )
    conn.commit()

    return redirect(row["original_url"], code=302)

# ---------------------------------------------------------
# 6. STATISTICS
# ---------------------------------------------------------
@app.get("/<code>/stats")
def get_stats(code):
    conn = get_db()
    row = conn.execute("SELECT * FROM urls WHERE code = ?",
                       (code,)
                       ).fetchone()
    if row is None:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    return jsonify({
        "code": row["code"],
        "original_url" : row["original_url"],
        "clicks": row["clicks"],
        "created_at": row["created_at"]
    })

# ---------------------------------------------------------
# 7. RUN SERVER
# ---------------------------------------------------------
if __name__ == "__main__":
    init_db()

    app.run(debug=True,
            port=5000)