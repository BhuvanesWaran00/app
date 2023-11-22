from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'
app.config['MYSQL_DATABASE_DB'] = 'data'
app.config['MYSQL_DATABASE_HOST'] = 'test.cwyp9bpkbyeg.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_PORT'] = 3306

mysql = pymysql.connect(
    host=app.config['MYSQL_DATABASE_HOST'],
    user=app.config['MYSQL_DATABASE_USER'],
    password=app.config['MYSQL_DATABASE_PASSWORD'],
    db=app.config['MYSQL_DATABASE_DB'],
    port=app.config['MYSQL_PORT']
)

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('mail')
    password = request.form.get('pass')

    # Create a MySQL cursor
    cursor = mysql.cursor()

    # Insert data into the 'users' table
    cursor.execute("INSERT INTO users (Name, Email, Password) VALUES (%s, %s, %s)", (name, email, password))

    # Commit changes to the database
    mysql.commit()

    # Close the cursor
    cursor.close()

    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    name = request.form.get('username')
    password = request.form.get('password')
    # Add any logic you need for the signin route
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
