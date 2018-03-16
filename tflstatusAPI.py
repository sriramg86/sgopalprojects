from json import dumps
import urllib.request, json
from flask import json, jsonify
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def tflstatuscall():
    outputjson = []
    with urllib.request.urlopen("https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status") as url:
        data = json.loads(url.read().decode())
    for idx, val in enumerate(data):
        item = {"id": idx}
        item["line"] = data[idx]['name']
        item["linestatus"] = data[idx]['lineStatuses'][0]['statusSeverityDescription']
        if 'reason' in data[idx]['lineStatuses'][0]:
            item["reason"] = data[idx]['lineStatuses'][0]['reason']
        else:
            item["reason"] = ''
        outputjson.append(item)
    return jsonify(outputjson)


class TubeStatus(Resource):
    def get(self):
        var_tube_status = tflstatuscall()
        return var_tube_status


api.add_resource(TubeStatus, '/tflstatus')  # Route_1


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0',port=5200)
