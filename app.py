import os
import pandas as pd
import plotly.express as px
from flask import Flask, request, render_template, send_file, make_response

from models.arima_model import arima_predict
from models.lr_model import lr_predict
from models.lstm_model import lstm_predict
from utils.data_utils import process_csv, generate_advice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    model_choice = request.form.get('model')
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        df = process_csv(filepath)

        if model_choice == 'ARIMA':
            forecast = arima_predict(df)
        elif model_choice == 'LinearRegression':
            forecast = lr_predict(df)
        elif model_choice == 'LSTM':
            forecast = lstm_predict(df)
        else:
            return "Please select a valid model"

        advice = generate_advice(forecast)

        forecast = forecast.reset_index(drop=True)
        forecast['Day'] = range(1, len(forecast)+1)
        fig = px.line(forecast, x='Day', y='Predicted Price', title='Price Prediction Trend', markers=True)
        graph_html = fig.to_html(full_html=False)

        # Save Excel file
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'forecast.xlsx')
        forecast.to_excel(excel_path, index=False)

        # Save HTML report (which can be printed as PDF)
        full_html = render_template('report.html',
                                     tables=[forecast.to_html(classes='data')],
                                     advice=advice,
                                     graph_html=graph_html,
                                     model_name=model_choice)
        
        report_path = os.path.join(app.config['UPLOAD_FOLDER'], 'forecast_report.html')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

        return render_template('result.html',
                               tables=[forecast.to_html(classes='data')],
                               advice=advice,
                               graph_html=graph_html)
    return "Please upload a CSV file"

@app.route('/download_excel')
def download_excel():
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'forecast.xlsx')
    if os.path.exists(path):
        return send_file(path, as_attachment=True, download_name='forecast.xlsx')
    return "Excel file not generated yet. Please upload and predict first.", 404

@app.route('/download_pdf')
def download_pdf():
    """Download the HTML report (can be saved as PDF from browser)"""
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'forecast_report.html')
    if os.path.exists(path):
        return send_file(path, as_attachment=True, download_name='forecast_report.html')
    return "Report not generated yet. Please upload and predict first.", 404

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
