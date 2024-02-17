from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/feature_importances', methods=['GET'])
def get_feature_importances():
    with open('feature_importance1.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
