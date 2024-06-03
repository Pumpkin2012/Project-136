from flask import Flask, jsonify, request
from data import data
app = Flask(__name__)
@app.route("/")
def immediate():
    return jsonify({
        "data":data,
        "message":"success"
    })
@app.route("/star")
def ask():
    star_name = request.args.get("name")
    star_data = next(item for item in data if item["name"]==star_name)
    return jsonify({
        "data":star_data,
        "message":"success"
    })
app.run()