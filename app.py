from flask import Flask, jsonify

app = Flask(__name__, static_url_path='')

@app.route('/similar')
def similar():
    return jsonify({
        "results": ["G04", "G10"]
    })

@app.route('/datasets')
def datasets():
    return jsonify({
        "results": [{
            "name": "Criminaliteitindex",
            "year": 2016,
            "id": "crim_index_2016"
        }, {
            "name": "Bevolking",
            "id": "count_2016",
            "year": 2016
        }]
    })

@app.route('/gemeentes')
def gemeentes():
    return jsonify({
        "results": [{
            "id": "G04",
            "name": "Arnhem"
        }, {
            "id": "G10",
            "name": "Nijmegen"
        }]
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
