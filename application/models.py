from application import db
from application import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash    # converte para hash e checa senhas
from flask_login import UserMixin   # implementa login ( is_authenticated, is_active, is_anonymous, get_id() )



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # nao é um campo, define o relacionamento com a tabela Post
    # backref sera o campo adicionado a tabela de 'muitos' (ou seja, Post)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # como sera impresso username
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


# carrega um usuario, dado seu id e passa para extensao flask-login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))