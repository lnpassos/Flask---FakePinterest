from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from fakepinterest import bcrypt


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# Model Usuario
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default="default_profile.png")
    fotos = database.relationship("Post", backref="usuario", lazy=True)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.senha, password)


# Model para as fotos Post
class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)