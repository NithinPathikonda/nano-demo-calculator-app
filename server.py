from flask import Flask, request, jsonify
from dataclasses import dataclass


@dataclass
class Result:
    result: int


app = Flask(_name_)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'


@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first = data.get('first')
    second = data.get('second')

    if first is None or second is None:
        return jsonify(error='Missing parameters'), 400

    result = first + second
    return jsonify(result=result)


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    first = data.get('first')
    second = data.get('second')

    if first is None or second is None:
        return jsonify(error='Missing parameters'), 400

    result = first - second
    return jsonify(result=result)


if _name_ == '_main_':
    app.run(port=8080, host='0.0.0.0')
