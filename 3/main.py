from flask import Flask , url_for , render_template , request
from werkzeug.utils import redirect
from custom_db import create_db , add_user , check_user , get_by_username

app = Flask(__name__ , template_folder='')
app.debug = True

@app.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        if 'login' in data.keys():
            username = data['username']
            password = data['password']
            db_data = get_by_username(username)
            print(db_data)
            if len(db_data) != 0:
                if username == db_data[0][0] and password == db_data[0][1]:
                    return render_template('fine.html')
            return render_template('index.html' , status='Неверный логин или пароль')
        elif 'signin' in data.keys():
            username = data['username']
            password = data['password']
            if not check_user(username):
                add_user(username , password)
                return render_template('index.html' , status='Пользователь успешно добавлен')
            else:
                return render_template('index.html' , status='Пользователь с таким именем уже существует')
    return render_template('index.html')

if __name__ == "__main__":
    create_db()
    app.run()