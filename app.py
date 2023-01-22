import pandas as pd
import traceback
from flask import Flask, request, jsonify, render_template
import pickle
import os
from datetime import date

app = Flask(__name__)
model = pickle.load(open('./model_Ada.pickle', 'rb'))

@app.route('/prediction', methods = ['POST'])
def prediction():
    try:
        json = request.get_json()
        df = pd.DataFrame(json, index=[0])
        prediction = model.predict(df)

        df['prediction'] = prediction
        df['call_timestamp'] = date.today()
        output_path='/shared/track.csv'
        df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))

        return df.iloc[0].to_json()

    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        return "Error: Invalid input data.", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

