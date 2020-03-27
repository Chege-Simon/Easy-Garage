from flask import Flask
from flask_bootstrap import Bootstrap

# Globally accessible libraries
bootstrap = Bootstrap()



def create_app():
    # initialize the core application
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    # intializing plugins
    bootstrap.init_app(app)

    # register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
 
from app import models