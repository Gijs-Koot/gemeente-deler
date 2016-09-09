from flask import Flask, jsonify, request
import feather
import json

app = Flask(__name__, static_url_path='')

df = feather.read_dataframe('./datasets/clean/clean_data.feather')
with open('./datasets/clean/columns.json') as f:
    column_data = json.load(f)

@app.route('/similar', methods=["POST"])
def similar():

    params = request.json
    print(params)

    gemeente_id = params["gemeente_id"]
    cats = params["categories"]

    return jsonify({
        "results": ["G04", "G10"],
        "request": params
    })

@app.route('/datasets')
def datasets():

    cols = [{
        "id": col
    } for col in df.columns if col in column_data]

    for c in cols:
        c.update(column_data[c["id"]])

    return jsonify(cols)

@app.route('/gemeentes')
def gemeentes():
    return jsonify({
        "results": [{
    "name": name,
    "id": int(index)
} for index, name in df[["regio"]].to_records()]
    })

@app.route('/gemeente')
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
