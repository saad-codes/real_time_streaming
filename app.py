from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'password'
mysql_database = 'sys'
mysql_port = 3307  # Use the mapped host port

# Connect to MySQL
db = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database,
    port=mysql_port
)

cursor = db.cursor()

# Check if the 'users' table exists, if not, create it
cursor.execute("SHOW TABLES LIKE 'users'")
result = cursor.fetchone()
print(result)
if not result:
    cursor.execute('''
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')
    db.commit()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    db.commit()
    return 'User added successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
