from flask import Flask, request, render_template, redirect,url_for

app = Flask(__name__)


@app.route('/')
def direct_login():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user == 'admin' and pwd == 'secret':
            return 'Welcome,admin!'
        else:
            return 'Invalid crendetial',401
    return render_template('sample_login.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)