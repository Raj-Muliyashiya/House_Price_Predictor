# House Price Prediction Project

An end-to-end Machine Learning web application that predicts real estate prices based on property features like location, square footage, and room count.

**Live Application:** [https://raj-muliyashiya-house-price-predictor.hf.space/](https://raj-muliyashiya-house-price-predictor.hf.space/)

---

## Project Overview

This project demonstrates the full Data Science pipeline, from data cleaning to model deployment. The goal was to build a tool that provides accurate property valuations to help users make informed real estate decisions.

**Key Technical Highlights:**
* **Data Processing:** Cleaned a dataset of 13,000+ records, handling missing values and inconsistent formatting.
* **Feature Engineering:** Implemented dimensionality reduction on location data to handle high cardinality.
* **Outlier Removal:** Applied business logic and statistical methods (Standard Deviation) to remove data errors and anomalies.
* **Model Selection:** Used GridSearchCV to compare algorithms (Linear Regression, Lasso, Decision Tree) and selected Linear Regression for best performance (~84% accuracy).
* **Deployment:** Built a REST API using FastAPI and deployed the model to Hugging Face Spaces.

## Technologies Used

* **Programming Language:** Python
* **Data Science Libraries:** Pandas, NumPy, Matplotlib
* **Machine Learning:** Scikit-Learn
* **Backend Framework:** FastAPI, Uvicorn
* **Deployment:** Hugging Face (Docker/Space)

## Installation & Setup

To run this project locally:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/House_Price_Prediction.git](https://github.com/YOUR_GITHUB_USERNAME/House_Price_Prediction.git)
    cd House_Price_Prediction
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the server**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Access the API**
    Open `http://127.0.0.1:8000/docs` in your browser to test the endpoints.

## API Usage

The application exposes an endpoint `/predict_home_price` that accepts JSON input:

**Input:**
```json
{
  "location": "Whitefield",
  "total_sqft": 1500,
  "bhk": 3,
  "bath": 3
}