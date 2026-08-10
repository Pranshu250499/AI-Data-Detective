# 🔎 AI Data Detective

AI Data Detective is an intelligent data analysis application built with Python and Streamlit.

It allows users to upload datasets and perform data cleaning, analysis, visualization, AI-powered insights, machine learning, and report generation from a single application.

## 🚀 Features

- 📤 Upload CSV and Excel datasets
- 📊 Dataset overview
- 🔍 Data analysis
- 📈 Interactive data visualization
- 🤖 AI-powered data insights
- 🧠 Machine learning model training
- 📋 Model comparison
- 📉 Model evaluation
- 📄 Report generation and download

## 🧠 Machine Learning

The application supports machine learning workflows for classification problems.

Currently implemented models include:

- Logistic Regression
- Decision Tree
- Random Forest

Users can:

1. Select a target column
2. Select the problem type
3. Choose the test-data percentage
4. Train multiple models
5. Compare model performance
6. View evaluation results

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Matplotlib
- Seaborn
- ReportLab
- OpenPyXL

## 📁 Project Structure

```text
AI-Data-Detective/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── pages/
│   ├── 0_Home.py
│   ├── 1_Upload_data.py
│   ├── 2_Data_Analysis.py
│   ├── 3_Data_Visualization.py
│   ├── 4_AI_Insights.py
│   ├── 5_Machine_Learning.py
│   └── 6_Report_Download.py
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── insights.py
│   └── ml_model.py
│
├── uploads/
│
└── venv/