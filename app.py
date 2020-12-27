from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from route import test, get_anime, return_all

data = [{'anime':["onepiece", "one piece"],'link':"alsdkfj","type":"action"},
        {'anime':["toriko"],'link':{'line':"alsdkfj"},"type":"action"},
        ]

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def home():
    return jsonify(data)

@app.route('/api')
def api():
    return jsonify(test())

@app.route('/get_name/<name>')
def get_name(name):
    return jsonify(get_anime(name))


if __name__ == '__main__':
    app.run(debug=True)
