# app.py
import logging
import os
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    logger.info("Handling request for /")
    return 'Hello, World!'

@app.route('/error')
def error():
    logger.error("This is an error log")
    return 'Error route', 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
