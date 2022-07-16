import secrets
from flask import Flask,render_template


def create_app():
    app = Flask(__name__)
    app = Flask(__name__)
    secret = secrets.token_urlsafe(23)
    app.secret_key = secret

    from website.views import views

    app.register_blueprint(views, url_prefix="/")

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.jinja2"), 404

    @app.errorhandler(500)
    def server_not_found(e):
        return render_template("500.jinja2"), 500
    return app