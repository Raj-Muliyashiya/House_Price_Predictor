# 🏡 Bengaluru House Price Prediction API

An End-to-End Machine Learning Project that predicts real estate prices in Bengaluru based on square footage, bathroom count, and location.

## 🚀 Overview
* **Problem:** Real estate prices are hard to estimate due to location variances.
* **Solution:** Built a Linear Regression model trained on 13,000+ properties.
* **Tech Stack:** Python, Scikit-Learn, Pandas, FastAPI.

## 📂 Project Structure
* `dataset/`: Contains the raw and cleaned CSV data.
* `model/`: Contains the trained `.pkl` model and `columns.json`.
* `server/`: Contains the FastAPI backend code (`main.py`).

## 🔧 How to Run Locally

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Bangalore_House_Price_Prediction.git](https://github.com/YOUR_USERNAME/Bangalore_House_Price_Prediction.git)
    cd Bangalore_House_Price_Prediction
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the API Server**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Test the API**
    Open your browser to `http://127.0.0.1:8000/docs`.
    Try the `/predict_home_price` endpoint with this JSON:
    ```json
    {
      "location": "Whitefield",
      "total_sqft": 1200,
      "bhk": 2,
      "bath": 2
    }
    ```

## 📊 Model Performance
The Linear Regression model achieves approximately **84% accuracy** (R2 Score) on the test dataset.
