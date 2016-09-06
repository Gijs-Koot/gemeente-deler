from flask import Flask

app = Flask(__name__, static_url_path='')

#@app.route('/<path:path>')
#def static(path):
#    return send_from_directory('static', path)

if __name__ == "__main__":

    app.run(debug=True)
