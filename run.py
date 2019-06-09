"""

modulo onde a app é executada

"""

from application import app, db
from application.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}



"""

ele conseguiu achar a variavel 'app' porque 
    'app' está num arquivo de nome '__init__'

"""