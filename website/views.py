from flask import Flask,render_template,Blueprint

views = Blueprint('views',__name__,static_folder='static', template_folder='templates')

@views.route("/")
def home():
    return render_template('home.jinja2')

