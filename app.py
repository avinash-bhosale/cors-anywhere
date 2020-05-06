from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/<path:path>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def index(path):
    headers = request.headers
    params = request.args
    json_data = request.json
    form_data = request.form.to_dict()
    if request.method == 'GET':
        response = requests.get(path, params=params, headers={'Authorization': headers.get('Authorization')})
        return jsonify(response.json()), response.status_code
    elif request.method == 'POST':
        response = requests.post(path, data=form_data, json=json_data, headers=headers)
        return jsonify(response.json()), response.status_code
    elif request.method == 'PUT':
        response = requests.put(path, data=form_data, json=json_data, headers=headers)
        return jsonify(response.json()), response.status_code
    return path


if __name__ == "__main__":
    app.run(debug=True, port=1234)
