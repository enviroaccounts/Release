from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

# Reading data
data_LUC = pd.read_excel("static/data/Template_LandUseChange.xlsx")
# print("data_LUC",data_LUC)
column_names = data_LUC.iloc[31, 2:9]  # C32 to I32
column_values = data_LUC.iloc[56, 2:9]  # C57 to I57
print("column_names",column_names)
PRINT("column_VALUES",column_values)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get_chart_data')
# def get_chart_data():
#     # Preparing data for D3.js
#     chart_data = []
#     for _, row in data_df.iterrows():
#         data_instance = {'name': row['category'], 'value': row['value']}
#         chart_data.append(data_instance)
    
#     return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)