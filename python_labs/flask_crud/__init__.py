from flask import Flask
from os import path
from flask_crud.models import User, Student, University, db
from flask_crud.views import views
from flask_crud.auth import auth
from flask_login import LoginManager
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ckdnvjksnvovod vsmdlkvnqwd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/university_db'
    db.init_app(app)
    migrate = Migrate(app, db)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    with app.app_context():
        db.create_all()

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
