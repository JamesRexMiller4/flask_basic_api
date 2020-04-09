from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys


def create_app(test_config=none):
  app = Flask(__name__)
  # VVVVVVVV - replace with setup_db(app)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/todoapp'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db = SQLAlchemy(app)
  migrate = Migrate(app, db)
  # alternatively can import from models directory
  CORS(app, resources={r='/api/*': {origins: '*'}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

  @app.route('/')
  @cross_origin
  def hello():
    return jsonify({"message": "Hello World!"})

  @app.route('/smile')
  def smile():
    return ':)'
  return app