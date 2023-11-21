from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('mail')
    password = request.form.get('pass')
    confirm_password = request.form.get('con_pass')
    print(name,email)
    return render_template('signin.html')
    
if __name__ == '__main__':
    app.run(debug=True)
