from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{soconnor70}:{password}@{dublinbikes.ctaptplk7c5t.eu-west-1.rds.amazonaws.com}/{dublinbikes}'
db = SQLAlchemy(app)

class Static(db.Model):
    __tablename__ = 'Stations'
    
    number = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    location_latitude = db.Column(db.FLOAT, nullable=False)
    location_longitude = db.Column(db.FLOAT, nullable=False)
    banking = db.Column(db.Boolean, nullable=False)
    bonus = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return '<Static %r>' % self.__tablename__
    