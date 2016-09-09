from flask import Flask, jsonify, request
import json
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import cm
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__, static_url_path='')
df = pd.read_csv("./datasets/clean/clean_data.csv", index_col=0)

normalizer = StandardScaler()
nn = NearestNeighbors()

def similar_gemeentes(gemeente_id, columns, n=5):

    values = df[columns].values

    values = normalizer.fit_transform(values)
    nn.fit(values)

    value = df.loc[gemeente_id][columns].values.reshape(1, -1)
    value = normalizer.transform(value)

    near = nn.kneighbors(value, n_neighbors=n)[1][0]

    return df.ix[df.index[near]]

with open('./datasets/clean/columns.json') as f:
    column_data = json.load(f)

import math


def num_fmt(num):
    i_offset = 15 # change this if you extend the symbols!!!
    prec = 3
    fmt = '.{p}g'.format(p=prec)
    symbols = ['Y', 'T', 'G', 'M', 'k', '', 'm', 'u', 'n']

    e = math.log10(abs(num))
    if e >= i_offset + 3:
        return '{:{fmt}}'.format(num, fmt=fmt)
    for i, sym in enumerate(symbols):
        e_thresh = i_offset - 3 * i
        if e >= e_thresh:
            return '{:{fmt}}{sym}'.format(num/10.**e_thresh, fmt=fmt, sym=sym)
    return '{:{fmt}}'.format(num, fmt=fmt)

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

    idx = sim.T.columns
    cols = sim.columns

    header = [""] + sim.T.loc["regio", idx].values.tolist() + ["Gemiddeld"]
    rows = sim.T.loc[list(set(cols) - {"regio"}), idx].rename(rename)
    rows["average"] = rows.apply(np.mean, axis=1)

    rows_formatted = rows.reset_index().values.tolist()

    from matplotlib.colors import rgb2hex

    def get_color(value, max=1):

        norm = matplotlib.colors.Normalize(vmin=-1 * max, vmax=max)
        cmap = cm.ScalarMappable(norm=norm, cmap=matplotlib.cm.jet)
        values = list(cmap.to_rgba(value))
        values[-1] = .001
        return rgb2hex(values)

    for row in rows_formatted:

        avg = row[-1]
        diff = [(val - avg) for val in row[1:-1]]
        max_diff = max([abs(d) for d in diff])


        for index in range(len(row)):
            value = row[index]

            if type(value) != float:
                row[index] = {
                    "value": value,
                    "color": None
                }
            else:

                this_diff = value - avg

                if value < 1:
                    row[index] = {
                        "value": "%.2f%%" % (float(value), ),
                        "color": get_color(this_diff, max=max_diff)
                    }

                else:
                    row[index] = {
                        "value": num_fmt(value),
                        "color": get_color(this_diff, max=max_diff)
                    }

    return jsonify({
        "header": header,
        "rows": rows_formatted
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
