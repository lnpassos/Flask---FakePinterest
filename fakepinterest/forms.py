from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

# Form Login
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirma = SubmitField("Fazer Login")

     # Campo para validar login 
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario or not usuario.check_password(self.senha.data):
            raise ValidationError("Email ou Senha inválidos!")
    

# Form para criação de conta
class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirma_senha = PasswordField("Confirmar Senha", validators=[DataRequired()])
    botao_confirma = SubmitField("Criar Conta") 

    # Validações 
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já Cadastrado!")

    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError("Usuário já Cadastrado!" )
        
    def validate_confirma_senha(self, confirma_senha):
        if confirma_senha.data != self.senha.data:
            raise ValidationError("As senhas devem ser iguais.")


# Form para Fotos
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirma = SubmitField("Enviar")

