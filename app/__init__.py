from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globally accessible libraries
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()



def create_app():
    # initialize the core application
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    # intializing plugins
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    # register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.customer import bp as customer_bp
    app.register_blueprint(customer_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        db.create_all()# create all the tables in the database


    return app
 
from app import models