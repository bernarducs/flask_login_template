"""

modulo que controla as páginas

"""

from application import app                                 # importando a app
from application.models import User
from application.forms import LoginForm                     # classe para login
from application import db
from application.forms import RegistrationForm
from flask import url_for                                   # gera urls usando o mapa interno de urls
from flask import render_template                           # responsavel por mandar dados para html
from flask import flash                                     # responsavel por mandar mensagens na tela
from flask import redirect                                  # redireciona para uma pag diferente
from flask_login import current_user                        # verifica se logado
from flask_login import login_user                          # registra usuario no ato de login
from flask_login import logout_user                         # executa logout
from flask_login import login_required                      # exige esta logado para certas pags
from flask import request                                   # todas as infos que usuario envia
from werkzeug.urls import url_parse                         # se uma url é relativa ou absoluta


@app.route('/')                                                         # pag inicial
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


# aceita tb o metodo post para enviar dados de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # se o usuario já está logado e entra na pag de login
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # processo de login
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()    # so preciso de 1 resultado
        if user is None or not user.check_password(form.password.data):

            # caso as infos sejam invalidas7
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # crendenciais corretas
        login_user(user, remember=form.remember_me.data)

        # redirecionamento
        next_page = request.args.get('next')                                # request.args funciona como dict

        # se nao ha next ou existe mas o caminho e absoluto
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)