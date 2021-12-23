"""
This script runs the FlaskTemplate application using a development server.
"""

from os import environ
from FlaskTemplate import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT)
