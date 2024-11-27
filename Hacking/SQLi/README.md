
`pip install flask flask-sqlalchemy`



### **1. Setting Up the Local HTTP Server**
You can use **Python**, **XAMPP**, or **Docker** to set up a local server. Let's use Python and Flask for simplicity.

#### Install Required Tools
- Python: Install from [python.org](https://www.python.org/downloads/).
- Install Flask and SQLite libraries:
  ```bash
  pip install flask flask-sqlalchemy
  ```

#### Create the Web Server Code
Save the following code as `app.py`:

```python
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
```

---

### **2. Run the HTTP Server**
Start the server on your local machine:
```bash
python app.py
```
This starts a local server accessible at `http://<YOUR_IP>:5000`. Replace `<YOUR_IP>` with your machine's IP address on the local network.

---

### **3. Perform SQL Injection on Another Device**
On another device in the same network, open a browser and navigate to `http://<YOUR_IP>:5000`. Use the following payloads to perform SQL Injection:

#### Example Inputs
- **Username**: `admin' --`
- **Password**: Leave blank.

This payload modifies the SQL query to:
```sql
SELECT * FROM users WHERE username = 'admin' -- ' AND password = '';
```
The `--` comments out the rest of the query, bypassing password verification.

#### Another Payload
- **Username**: `' OR '1'='1`
- **Password**: Leave blank.

This changes the query to:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '';
```
Since `'1'='1'` is always true, the login succeeds.

---

### **4. Observe and Understand**
- Open the server terminal to see the executed SQL queries. Notice how the input modifies the SQL logic.
- Demonstrate how attackers manipulate inputs to extract or manipulate data.

---

### **5. Safe Cleanup**
After finishing:
- Stop the server.
- Delete the `example.db` file to remove the test database.

---

### **Key Points to Emphasize in the Demonstration**
1. **Query Vulnerability**: Show how unsanitized inputs directly modify SQL logic.
2. **Prevention**: Compare with a secure query using parameterized statements.
3. **Real-World Risks**: Highlight how attackers could extract sensitive data or take over accounts.

This setup creates a safe, controlled environment to understand SQLi risks and prevention strategies.





















If the earlier script didn’t meet your needs, here's a revised approach using Flask and a simple SQLite database. This version ensures the demonstration works correctly for SQL Injection scenarios, including query manipulation. Follow the updated instructions closely.

---

### **Complete Script: `sqli_demo_revised.py`**

```python
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
```

---

### **How to Set Up and Use**
#### 1. **Install Python and Flask**
   - Install Python: [Download Python](https://www.python.org/downloads/).
   - Install Flask:
     ```bash
     pip install flask
     ```

#### 2. **Run the Script**
   - Save the file as `sqli_demo_revised.py`.
   - Run the server:
     ```bash
     python sqli_demo_revised.py
     ```
   - Access it on a browser via `http://<YOUR_IP>:5000`.

#### 3. **SQL Injection Demonstration**

1. **Login Page**
   - URL: `http://<YOUR_IP>:5000/login`
   - Payloads:
     - Username: `admin' --`
       - Logs in as admin.
     - Username: `' OR '1'='1`
       - Bypasses login check.

2. **Search Page**
   - URL: `http://<YOUR_IP>:5000/search`
   - Payload:
     - Keyword: `' OR '1'='1`
       - Fetches all users.

3. **User Details Page**
   - URL: `http://<YOUR_IP>:5000/user?id=1`
   - Payload:
     - Change `id=1` to `id=1 OR 1=1`
       - Returns all users.

---

### **What You Learn**
1. **How SQL Queries Are Injected:**
   - Observe how user inputs modify the SQL queries in logs.

2. **How to Secure:**
   - Discuss parameterized queries:
     ```python
     query = "SELECT * FROM users WHERE username = ? AND password = ?"
     cursor.execute(query, (username, password))
     ```

3. **Real-World Impact:**
   - Highlight how vulnerable endpoints can lead to database leaks or admin bypass.

---

### **Notes**
This script avoids excessive complexity while remaining practical. It logs each query for educational purposes, making it ideal for a hands-on demonstration. Let me know if adjustments are needed!