from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_etf_data', methods=['GET'])
def get_etf_data():
    # For demonstration, let's generate data here. In real app, fetch from a database or external API.
    dates = pd.date_range(start="2023-01-01", periods=20)
    np.random.seed(0)
    opens = 370 + np.random.normal(0, 2, 20).cumsum()
    highs = opens + np.random.normal(1, 2, 20)
    lows = opens - np.random.normal(1, 2, 20)
    closes = opens + np.random.normal(0, 1.5, 20)
    adj_closes = closes * 0.98
    volumes = np.random.randint(100000, 500000, 20)
    data = pd.DataFrame({
        'Date': dates.strftime('%Y-%m-%d'),  # format dates as strings for JSON
        'Open': opens,
        'High': highs,
        'Low': lows,
        'Close': closes,
        'Adjusted Close': adj_closes,
        'Volume': volumes
    })
    return jsonify(data.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
