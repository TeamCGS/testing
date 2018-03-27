#from flask import Flask
#from flask_sqlalchemy import SQLAlchemye
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{soconnor70}:{password}@{dublinbikes.ctaptplk7c5t.eu-west-1.rds.amazonaws.com}/{dublinbikes}'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<soconnor70>:<password>@<dublinbikes.ctaptplk7c5t.eu-west-1.rds.amazonaws.com>/<https://eu-west-1.console.aws.amazon.com/rds/home?region=eu-west-1#dbinstance:id=dublinbikes>'
engine = create_engine('mysql+mysqlconnector://CGSdatabase:password@dublinbikes.ctaptplk7c5t.eu-west-1.rds.amazonaws.com/dublinbikes')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)