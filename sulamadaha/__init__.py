from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()



app = Flask('__name__', template_folder='sulamadaha/templates', static_folder='sulamadaha/static')
app.config['SECRET_KEY'] = "restywaniaurellia"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sulamadaha.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt.init_app(app)

from sulamadaha.pengguna.routes import rpengguna
from sulamadaha.admin.routes import radmin
from sulamadaha.penjual.routes import rpenjual
app.register_blueprint(rpengguna)
app.register_blueprint(radmin)
app.register_blueprint(rpenjual)

