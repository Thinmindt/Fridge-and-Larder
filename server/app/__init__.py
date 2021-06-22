from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
  app = Flask(__name__)
  app.debug = True
  
  if test_config is None:
    app.config.from_object(Config)
  else:
    app.config.update(test_config)

  db.init_app(app)
  migrate.init_app(app, db)
  CORS(app)

  from app.graphene import bp as graphene_bp
  app.register_blueprint(graphene_bp)
  
  return app

from app import models