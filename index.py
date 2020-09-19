import json
from flask import abort, Flask, Blueprint, jsonify, request
from src.data_manager import DataManager


data_manager = DataManager()

app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')


@app.route('/')
def index():
    return jsonify({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


app.register_blueprint(apiv1)
