from flask import Flask, jsonify
from config import Config
from db import get_db_connection

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return "Welcome to the Capstone Project API"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    # Convert the fetched rows to a list of dicts if needed
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)