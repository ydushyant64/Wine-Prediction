# 🍷 Wine Quality Prediction Web App

A simple machine learning web application that predicts the quality of wine on a scale from 3 to 8 based on its physicochemical properties. This project takes a trained model and deploys it using the Flask web framework.

---

## ✨ Live Demo

You can try the live application here:

**[https://wine-prediction-j7km.onrender.com/](https://wine-prediction-j7km.onrender.com/)**


![Screenshot of the Wine Quality Prediction App](sreenshot.PNG)

## 📊 Input Parameter Ranges

To get a prediction, please provide values within the following ranges, which are typical for this dataset.

| Parameter | Min Value | Max Value |
| :--- | :--- | :--- |
| **Fixed Acidity** | 4.6 | 15.9 |
| **Volatile Acidity**| 0.12 | 1.58 |
| **Citric Acid** | 0.0 | 1.0 |
| **Residual Sugar**| 0.9 | 15.5 |
| **Chlorides** | 0.012 | 0.611 |
| **Free Sulfur Dioxide**| 1.0 | 72.0 |
| **Total Sulfur Dioxide**| 6.0 | 289.0 |
| **Density** | 0.99 | 1.003 |
| **pH** | 2.74 | 4.01 |
| **Sulphates** | 0.33 | 2.0 |
| **Alcohol** | 8.4 | 14.9 |

> ***Note:*** *These values are standard for the dataset. To get the exact ranges for your specific `wine_data.csv` file, run `df.describe()` in your Jupyter notebook and update the table above.*

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML/Data:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS

---

## 🚀 How to Run Locally

To run this project on your local machine, follow these steps.

**1. Clone the repository:**
```bash
git clone [https://github.com/ydushyant64/Wine-Prediction.git](https://github.com/ydushyant64/Wine-Prediction.git)
cd Wine-Prediction
