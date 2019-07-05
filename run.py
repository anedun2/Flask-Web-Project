from flaskblog import create_app
import logging
from logging.handlers import RotatingFileHandler
from flaskblog.errors import handlers

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
logger = logging.getLogger('flaskblog')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(file_handler)
# 'application' code
