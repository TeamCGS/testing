import os
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('test_dublinBikes.default_settings')
app.config.from_envvar('TEST_DUBLINBIKES_SETTINGS')
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'test_dublinBikes.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import test_dublinBikes.views
