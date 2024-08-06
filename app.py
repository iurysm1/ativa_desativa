from flask import Flask, request, redirect, render_template, flash, jsonify
from flask.helpers import url_for
from flask_login import login_required, login_user, current_user, LoginManager, logout_user
from config import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from desativarAtivarRede import resetaPlacaDeRede



app = Flask(__name__)

DB = "database.db"

app.config['SECRET_KEY'] = 'getic000@'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB}'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view='/login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)




@app.route("/reset", methods=["POST"])
def reset():
    resetaPlacaDeRede()
    return jsonify({})



@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=='POST':
        user= request.form.get('user')
        senha= request.form.get('senha')

        user = User.query.filter_by(username=user).first()
        if user:
            if check_password_hash(user.password, senha):
                flash('Login efetuado com sucesso', category='sucess')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Senha incorreta', category='error')
        else:
            flash('Usuário não cadastrado', category='error')

    return render_template("login.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__== "__main__":
    app.run(debug=True)
