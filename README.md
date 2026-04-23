```markdown
# AgriPredict Platform

A web-based platform for predicting agricultural product prices using **ARIMA**, **Linear Regression**, and **LSTM** models.  
Users can upload CSV files with historical data, generate price forecasts, view interactive charts, and download results as Excel/HTML files.

---

## Features

- Upload CSV files with historical price, production, and demand data
- Predict future prices using multiple models: ARIMA, Linear Regression, LSTM
- Interactive Plotly charts for forecast visualization
- Strategy suggestions based on predicted trends
- Download forecast results as Excel and HTML report
- Responsive web interface with progress bar
- Optional: Share the site via **ngrok** for remote access

---

## File Structure

```
agri_predict_platform/
├── app.py              # Main Flask app
├── requirements.txt    # Python dependencies
├── models/             # Model scripts (ARIMA, LR, LSTM)
│   ├── arima_model.py
│   ├── lr_model.py
│   └── lstm_model.py
├── utils/              # Data processing and advice scripts
│   └── data_utils.py
├── templates/          # HTML templates
│   ├── index.html
│   ├── result.html
│   └── report.html
├── static/             # CSS, JS, images
└── uploads/            # Folder to store uploaded CSV and results
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/agri-predict.git
cd agri-predict
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the Flask server:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

You should see the **AgriPredict Platform** homepage where you can upload CSV files and select a model.

---

## Using ngrok for Public Access (Optional)

If you want to share the app with others:

1. Install [ngrok](https://ngrok.com) and authenticate:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

2. Start a tunnel to your local Flask server:

```bash
ngrok http 5000
```

3. ngrok will give a public HTTPS URL (e.g., `https://abcd1234.ngrok-free.app`)

4. Share this URL — anyone with internet access can use your platform.

> **Note:** Free ngrok URLs change each session. Keep both Flask and ngrok running.

---

## CSV File Format

Example CSV structure:

```csv
Date,Price,Production,Demand
2025-06-01,24.67,1200,1100
2025-07-01,24.85,1180,1150
2025-08-01,25.10,1250,1200
```

- **Date:** `YYYY-MM-DD` format
- **Price:** Historical product price (e.g., yuan/kg)
- **Production:** Monthly production volume
- **Demand:** Monthly demand volume

---

## Model Selection Guide

| Model | Best For | Requirements |
|-------|----------|--------------|
| **ARIMA** | Time series with clear trends | Price column only |
| **Linear Regression** | Linear relationships with features | Price + Production + Demand |
| **LSTM** | Complex non-linear patterns | Larger datasets recommended |

---

## Notes

- Ensure `uploads/` folder exists with write permission for saving files
- ARIMA works best with at least 10 data points
- Linear Regression uses Production and Demand as features
- LSTM may take longer to train depending on data size
- The HTML report can be printed as PDF from the browser (`Ctrl+P`)

---

## License

This project is for educational and prototype purposes.  
Do not use for commercial production without proper adjustments.
```

---
