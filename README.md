# PhishingThesis
This is especially created to document my work which i will be to complete my thesis.
# 📧 Spam Email Detection with Machine Learning

This project uses Natural Language Processing (NLP) and machine learning to classify SMS messages as spam or ham.

## 📁 Dataset
- Source: [UCI SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- Total messages: 5,574

## 🤖 Models Used
- Logistic Regression
- Random Forest Classifier

## 📊 Performance
- Accuracy: ~98%
- Spam Recall: ~82%
- Confusion Matrix:  
  - True Ham: 966  
  - True Spam: 122  
  - False Negatives: 27  
  - False Positives: 0

## 🔍 Top Spam Keywords
`txt`, `call`, `claim`, `free`, `prize`, etc.

## 📓 How to Use
Open the notebook here:  
[spam_detector.ipynb](https://github.com/shani123/PhishingThesis/blob/main/spam_detector.ipynb)

Run it in Google Colab to retrain or test with your own messages.

## 📦 Requirements
Install the following Python libraries:

```bash
pip install pandas scikit-learn matplotlib seaborn
