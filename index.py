import json
from flask import abort, Flask, Blueprint, jsonify, request
from flask_cors import cross_origin
from src.data_manager import DataManager


data_manager = DataManager()

app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')


@app.route('/')
def index():
    return jsonify({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/prefectures')
@cross_origin(apiv1)
def prefectures():
    return data_manager.prefectures_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


app.register_blueprint(apiv1)
