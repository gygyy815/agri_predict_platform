# AgriPredict Platform

A web-based platform for predicting agricultural product prices using **ARIMA**, **Linear Regression**, and **LSTM** models.  
Users can upload CSV files with historical data, generate price forecasts, view interactive charts, and download results as Excel files.

---

## Features

- Upload CSV files with historical price, production, and demand data  
- Predict future prices using multiple models: ARIMA, Linear Regression, LSTM  
- Interactive Plotly charts for forecast visualization  
- Strategy suggestions based on predicted trends  
- Download forecast results as Excel  
- Optional: Share the site via **ngrok** for remote access  

---

## File Structure


agri_predict_platform/
├─ app.py # Main Flask app
├─ requirements.txt # Python dependencies
├─ /models # Model scripts (ARIMA, LR, LSTM)
├─ /utils # Data processing and advice scripts
├─ /templates # HTML templates (index.html, result.html)
├─ /static # CSS, JS, images
├─ /uploads # Folder to store uploaded CSV and results


---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/agri-predict.git
cd agri-predict
Create a virtual environment and activate it
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Running the Project

Start the Flask server:

python app.py

Open your browser and go to:

http://127.0.0.1:5000

You should see the AgriPredict Platform homepage where you can upload CSV files and select a model.

Using ngrok for Public Access (Optional)

If you want to share the app with others:

Install ngrok (https://ngrok.com
) and authenticate:
ngrok config add-authtoken YOUR_AUTH_TOKEN
Start a tunnel to your local Flask server:
ngrok http 5000
ngrok will give a public HTTPS URL (e.g., https://abcd1234.ngrok-free.app)
Share this URL; anyone with internet access can use your platform.

Note: Free ngrok URLs change each session. Keep Flask and ngrok running.

CSV File Format

Example CSV structure:

Date,Price,Production,Demand
2025-06-01,24.67,1200,1100
2025-07-01,24.85,1180,1150
2025-08-01,25.10,1250,1200
...
Date: YYYY-MM-DD
Price: Historical product price (e.g., yuan/kg)
Production: Monthly production
Demand: Monthly demand
Notes
Use ARIMA for time series trend prediction
Linear Regression requires Production and Demand columns
LSTM may take longer to train depending on data size
Ensure uploads/ folder exists with write permission for saving files
License

This project is for educational and prototype purposes.
Do not use it for commercial production without proper adjustments.
