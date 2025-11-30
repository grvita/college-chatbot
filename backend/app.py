from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from chatbot_logic import find_response

app = Flask(__name__)
CORS(app)


def get_db():
    conn = sqlite3.connect('../database/college.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/login")
def login():
    data = request.get_json()
    enrollment_no = data.get("enrollment_no", "").strip()

    if not enrollment_no:
        return jsonify({"success": False, "message": "Enrollment number is required"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT enrollment_no, name, branch, year_sem FROM students WHERE enrollment_no = ?",
        (enrollment_no,)
    )
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({"success": False, "message": "Enrollment not found. Please contact admin."}), 404

    return jsonify({
        "success": True,
        "student": {
            "enrollment_no": row["enrollment_no"],
            "name": row["name"],
            "branch": row["branch"],
            "year_sem": row["year_sem"],
        }
    }), 200

@app.post("/chat")
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = find_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
