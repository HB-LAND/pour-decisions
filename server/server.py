"""Server for pour-decisions app."""

from flask import (Flask, render_template, request, session, jsonify)
from model import connect_to_db

app = Flask(__name__)

#============================     PAGE ROUTES    ==================================#

#landing page


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
