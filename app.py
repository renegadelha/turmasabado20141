from flask import *

import dao

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/fazerlogin', methods=['POST'])
def logar():
    login = request.form.get('login')
    senha = request.form.get('senha')

    if dao.verificar_login(login, senha):
        return render_template('home.html', user=login)
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)