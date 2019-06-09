"""

modulo onde a app é criada

"""

from flask import Flask    # importa flask
from config import Config   # import config mesmo estando um diretorio acima
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# cria um app
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'    # forca usuario nao logado a fazer login sempre redirecionando a pag de login

from application import routes, models

"""
    OBS: o pacote 'application' é definido pelo diretório 'application'
"""