from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'                                                                     # 'your_mysql_username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'                                                              # 'your_mysql_password'
app.config['MYSQL_DATABASE_DB'] = 'data'                                                                        # 'your_mysql_database'
app.config['MYSQL_DATABASE_HOST'] = 'test.cwyp9bpkbyeg.ap-south-1.rds.amazonaws.com'                            # 'your_mysql_host'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('mail')
    password = request.form.get('pass')

        # Create a MySQL cursor
    cursor = mysql.get_db().cursor()

    # Insert data into the 'users' table
    cursor.execute("INSERT INTO users (Name, Email, Password) VALUES (%s, %s, %s)", (name, email, password))

    # Commit changes to the database
    mysql.get_db().commit()

    # Close the cursor
    cursor.close()

    return render_template('signin.html')

@app.route('/signin.html')
def signin():
    name = request.form.get('username')
    password = request.form.get('password')
    # Add any logic you need for the signin route
    return render_template('signin.html')
    
if __name__ == '__main__':
    app.run(debug=True)
