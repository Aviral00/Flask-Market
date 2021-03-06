from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '085b3eb33e4614fef65e7556'
db = SQLAlchemy(app)
from market import routes