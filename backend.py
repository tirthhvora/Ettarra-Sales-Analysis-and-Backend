from flask import Flask, jsonify
import json
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

app = Flask(__name__)


with open('rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

X_test = pd.read_csv('testing_data.csv') 

@app.route('/feature_importances', methods=['GET'])
def get_feature_importances():
        
        feature_importances = pd.DataFrame({'Feature': X_test.columns, 'Importance': rf_model.feature_importances_})
        feature_importances_sorted = feature_importances.sort_values(by='Importance', ascending=False)

        data = feature_importances_sorted.to_dict(orient='records')
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
