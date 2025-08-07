from flask import Flask
from flask_pymongo import PyMongo
from flasgger import Swagger
from dotenv import load_dotenv
load_dotenv()

mongo = PyMongo()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    mongo.init_app(app)
    #http://localhost:8000/apidocs/
    swagger.init_app(app)
    
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    
    return app