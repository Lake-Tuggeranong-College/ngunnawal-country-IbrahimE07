from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, SubmitField, IntegerField, PasswordField, FileField
from flask_wtf.file import FileRequired
<<<<<<< HEAD
# from models import User
=======
from models import User
>>>>>>> d5b247a (Database, Contact us page working)

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"class": "border border-primary rounded text-primary bg-light"})
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"class": "border border-primary rounded text-primary bg-light"})
    message = StringField("Message", validators=[DataRequired()], render_kw={"class": "border border-primary rounded text-primary bg-light"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary btn-block"})
