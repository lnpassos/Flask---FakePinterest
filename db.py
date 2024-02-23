# Gerar banco de dados!

from fakepinterest import database, app
from fakepinterest.models import Usuario, Post

with app.app_context():
    database.create_all()