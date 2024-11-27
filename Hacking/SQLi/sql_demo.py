from flask import Flask, request, make_response
import sqlite3

app = Flask(__name__)

DATABASE = 'demo.db'

# Initialize the database
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
    # Insert sample data
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'password')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (2, 'user1', '12345')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (3, 'test', 'testpass')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return '''
        <h1>SQL Injection Demonstration</h1>
        <ul>
            <li><a href="/login">Login Page</a></li>
            <li><a href="/search">Search Page</a></li>
            <li><a href="/user?id=1">User Details</a></li>
        </ul>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Vulnerable Query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return f"<h1>Welcome, {result[1]}!</h1>"
        else:
            return "<h1>Login Failed!</h1>"
    return '''
        <h1>Login</h1>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Vulnerable Query
        query = f"SELECT * FROM users WHERE username LIKE '%{keyword}%'"
        print(f"Executing query: {query}")
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        
        if results:
            return f"<h1>Search Results:</h1> <pre>{results}</pre>"
        else:
            return "<h1>No Results Found!</h1>"
    return '''
        <h1>Search Users</h1>
        <form method="POST" action="/search">
            Search Keyword: <input type="text" name="keyword"><br>
            <button type="submit">Search</button>
        </form>
    '''

@app.route('/user')
def user_details():
    user_id = request.args.get('id')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Vulnerable Query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    print(f"Executing query: {query}")
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return f"<h1>User Details</h1> <p>ID: {user[0]}, Username: {user[1]}</p>"
    else:
        return "<h1>User Not Found!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
