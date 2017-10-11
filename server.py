from flask import Flask
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


trades = db.Table('trades',
        db.Column('coin_id', db.Integer, db.ForeignKey('coin.id')),
        db.Column('exc_id', db.Integer, db.ForeignKey('exchange.id'))
)


class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), primary_key=True)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.now)


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    coins = db.relationship('Coin', secondary=trades, backref=db.backref('traded_at', lazy='dynamic'))


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Coin, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Exchange, methods=['GET'])

# start the flask loop
app.run()