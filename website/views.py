from flask import render_template,Blueprint,flash,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SearchField, TextAreaField
from wtforms.validators import DataRequired,Email
from .sender import to_client,to_admin

views = Blueprint('views',__name__,static_folder='static', template_folder='templates')
#Create contact class
class ContactForm(FlaskForm):
    Email = StringField('Email Address', validators=[DataRequired()])
    Subject = StringField('Subject', validators=[DataRequired()])
    Message = TextAreaField('Message', validators=[DataRequired()])
    Submit = SubmitField("Submit")

@views.route("/")
def home():
    return render_template('home.jinja2')

@views.route("/about")
def about_us():
    return render_template('aboutus.jinja2')

@views.route("/contact", methods=['POST', "GET"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        Email = form.Email.data
        Subject = form.Subject.data
        Message = form.Message.data

        to_client(Email)
        to_admin(Email, Message, Subject)
        return redirect(url_for("views.submitted"))

    return render_template('contact_me.jinja2', form= form)


@views.route("/projects/alley")
def bowling():
    return render_template('bowling.jinja2')

@views.route("/submitted", methods =["POST","GET"])
def submitted():
    flash("Message was successfully received", category="success")
    return render_template("reply.jinja2")

@views.route("/projects")
def projects():
    return render_template("projects.jinja2")

@views.route("/projects/interior")
def interiors():
    return render_template("interiors.jinja2")

@views.route("/projects/institutions")
def institutions():
    return render_template("institutions.jinja2")

@views.route("/projects/residents")
def residents():
    return render_template("residents.jinja2")