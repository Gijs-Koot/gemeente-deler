from flask import Flask, jsonify, request
import feather
import json
from sklearn.neighbors import NearestNeighbors
import numpy as np


app = Flask(__name__, static_url_path='')
df = feather.read_dataframe('./datasets/clean/clean_data.feather').dropna()

nn = NearestNeighbors()

def similar_gemeentes(gemeente_id, columns, n=5):

    values = df[columns].values

    nn.fit(values)
    near = nn.kneighbors(df.loc[gemeente_id][columns].values.reshape(1, -1), n_neighbors=n)[1][0]

    return df.ix[df.index[near]]

with open('./datasets/clean/columns.json') as f:
    column_data = json.load(f)

@app.route('/similar', methods=["POST"])
def similar():

    params = request.json
    print(params)

    gemeente_id = int(params["gemeente_id"])
    cats = params["categories"]

    sim = similar_gemeentes(gemeente_id, cats)

    idx = sim.T.columns
    cols = sim.columns

    rename = {
        key: value["name"] for key, value in column_data.items()
    }

    print(sim.head())

    idx = sim.T.columns
    cols = sim.columns

    header = [""] + sim.T.loc["regio", idx].values.tolist() + ["average"]
    rows = sim.T.loc[list(set(cols) - {"regio"}), idx]

    rows["average"] = rows.apply(np.mean, axis=1)

    rows = rows.rename(rename).reset_index().values.tolist()

    return jsonify({
        "header": header,
        "rows": rows
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
