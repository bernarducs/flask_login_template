"""

arquivo onde ficarao as variaveis que configuram a app

"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))    # diretorio da app


class Config(object):                                    # classe que armazena variaveis de configuracao

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False