from flask import Flask, Blueprint, jsonify
from flask_cors import cross_origin
from src.data_manager import DataManager


data_manager = DataManager()

app = Flask(__name__)

apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')


@app.route('/')
def index():
    return jsonify({'message': 'Web API to get COVID-19(coronavirus) information of each prefecture in Japan.'})


@apiv1.route('/death_daily')
@cross_origin(apiv1)
def death_daily():
    return data_manager.death_daily_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/effective_reproduction')
@cross_origin(apiv1)
def effective_reproduction():
    return data_manager.effective_reproduction_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/pcr_positive_daily')
@cross_origin(apiv1)
def pcr_positive_daily():
    return data_manager.pcr_positive_daily_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/pcr_tested_daily')
@cross_origin(apiv1)
def pcr_tested_daily():
    return data_manager.pcr_tested_daily_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/prefectures')
@cross_origin(apiv1)
def prefectures():
    return data_manager.prefectures_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


@apiv1.route('/serious')
@cross_origin(apiv1)
def serious():
    return data_manager.serious_json, 200, {'Content-Type': 'application/json; charset=utf-8'}


app.register_blueprint(apiv1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
