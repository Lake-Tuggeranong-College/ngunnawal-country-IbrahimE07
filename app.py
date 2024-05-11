from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, LoginManager, logout_user, login_required

app = Flask(__name__)
app.config.from_object(Config)  # loads the configuration for the database
db = SQLAlchemy(app)  # creates the db object using the configuration
login = LoginManager(app)
login.login_view = 'login'

<<<<<<< HEAD
# from forms import ContactForm, LoginForm, RegistrationForm, ResetPasswordForm, UserProfileForm
from models import User, Contact

=======
from forms import ContactForm
from models import Contact
>>>>>>> d5b247a (Database, Contact us page working)



@app.route('/')
def homepage():  # put application's code here
    return render_template("index.html", title="Homepage")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(new_contact)
        db.session.commit()
        # flash("Your message has been sent to administrators.")
        return redirect(url_for("homepage"))
    return render_template("contact.html", title="Contact Us", form=form, user=current_user)
<<<<<<< HEAD

=======
>>>>>>> d5b247a (Database, Contact us page working)

@app.route('/gallery')
def gallery():  # put application's code here
    return render_template("gallery.html", title="Photo Gallery")


@app.route('/history')
def history():  # put application's code here
    return render_template("history.html", title="History of Ngunnawal")

@app.route('/grid')
def grid():  # put application's code here
    return render_template("grid.html", title="Bootstrap Grid")



if __name__ == '__main__':
    app.run()
