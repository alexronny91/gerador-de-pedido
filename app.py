from flask import Flask, request, flash, render_template
from database import db
from flask_migrate import Migrate
from routes import bp

app = Flask(__name__)


app.config['SECRET_KEY'] = "MySeCrET@123321"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_gerador_de_pedido.db'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp)

db.init_app(app)
migrate = Migrate(app, db)

app.run(debug = True)
