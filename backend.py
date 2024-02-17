from flask import Flask, jsonify
import json
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error

app = Flask(__name__)


with open('rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

X_test = pd.read_csv('testing_data.csv') 
sales= pd.read_csv('Sales_Data.csv')
                   

@app.route('/feature_importances', methods=['GET'])
def get_feature_importances():

        feature_importances = pd.DataFrame({'Feature': X_test.columns, 'Importance': rf_model.feature_importances_})
        feature_importances_sorted = feature_importances.sort_values(by='Importance', ascending=False)

        data = feature_importances_sorted.to_dict(orient='records')
        return jsonify(data)

@app.route('/top-item-sales', methods=['GET'])
def get_top_item_sales():
    item_sales = sales.groupby('Item Name')['Final Total'].sum().sort_values(ascending=False)
    top_items = item_sales.head(15)
    
    top_items_sales_list = [{'item': item, 'sales': sales} for item, sales in zip(top_items.index, top_items.values)]
    
    top_items_sales_json = jsonify(top_items_sales_list).response[0]
    
    return top_items_sales_json


     


if __name__ == '__main__':
    app.run()
