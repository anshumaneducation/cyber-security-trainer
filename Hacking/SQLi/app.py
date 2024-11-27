from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'example.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    conn.commit()
    conn.close()

init_db()

# Vulnerable route
@app.route('/')
def login_page():
    return '''
        <h1>Login</h1>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vulnerable SQL query
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # Log the query for debugging
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return "<h1>Login Successful</h1>"
    else:
        return "<h1>Login Failed</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
