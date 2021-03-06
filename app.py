from flask import Flask, jsonify, request
import json
import numpy as np
import pandas as pd

from gemdel import similar_gemeentes

app = Flask(__name__, static_url_path='')
df = pd.read_csv("./datasets/clean/clean_data.csv", index_col=0)

with open('./datasets/clean/columns.json') as f:
    column_data = json.load(f)

@app.route('/api/similar', methods=["POST"])
def similar():

    params = request.json
    print(params)

    gemeente_id = int(params["gemeente_id"])
    cats = params["categories"]

    sim = similar_gemeentes(df, gemeente_id, cats).T

    print(sim)

    return jsonify({
        "results": list(json.loads(sim.to_json()).values())
    })

@app.route('/api/datasets')
def datasets():

    cols = [{
        "id": col
    } for col in df.columns if col in column_data]

    for c in cols:
        c.update(column_data[c["id"]])

    return jsonify(cols)

@app.route('/api/gemeentes')
def gemeentes():
    return jsonify({
        "results": [{
    "name": name,
    "id": int(index)
} for index, name in df[["regio"]].to_records()]
    })

@app.route('/api/gemeente')
def gemeente():
    return jsonify({
        "result": {
            "name": "Arnhem",
            "id": "G04",
            "crimality": .4,
            "count": 123
        }
    })


if __name__ == "__main__":

    app.run(debug=True)
