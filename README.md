# Clothes Size Prediction

This is a Flask web application that uses a Machine Learning model to predict clothing sizes based on user inputs such as age, height, and weight. The project demonstrates the integration of a machine learning model with a web interface for practical use.

# Project Details
## This project has four pages:
### 1. Main Page (Homepage)
   ![image](https://github.com/user-attachments/assets/44966035-511b-4bd8-9074-a453d77349c0)
   Serves as the landing page, introducing users to the website’s features. It contains a navigation bar and three clickable cards representing the key functionalities.
### 2. Clothes Size Prediction
   ![image](https://github.com/user-attachments/assets/87aca847-99ab-4873-94ba-b720c3575ae5)
   A page where users input their age, height, and weight to receive a predicted clothing size based on a trained machine learning model. This page load pickle file to store the model for web loading efficiency. However, the pickle file is too large to upload to GitHub. Please run the training_model.py first before starting the flask app.
### 3. Outfit Color Calculator
   ![image](https://github.com/user-attachments/assets/b0993e96-4896-40bd-a0c2-6c771439c3da)
   Helps users choose matching outfit colors by allowing them to select a base color and receiving recommendations for complementary colors.
### 4. Outfit for My Skintone
   ![image](https://github.com/user-attachments/assets/17716e46-092e-4502-9280-56068f161ff0)
   Suggests outfit colors that best match the user’s skin tone, providing personalized fashion advice.

## The steps to do the peroject includes:
### 1. Data Preparation
   Getting data clothes_size.csv from Kaggle.
### 2. Data Pre-processing
   Removing null values
### 3. Model Training
   Train model using RandomForestClassifier and save it to pickle file. This algorithm is chosen based on evaluation result.
### 4. Evaluating Model
   The model resulting in 50.69% accuracy for RandomForest Classifier. Although SVM gives higher accuracy, its speed is worse than RandomForestClassifier. So, RandomForestClassifier is chosen.
   
   ![image](https://github.com/user-attachments/assets/ed8ad620-b556-4a8b-a5dd-e7e62a254035)
### 5. Deploying Machine Learning Model to web
   Once the model is trained and evaluated, it is deployed as a web application using Flask. The trained size_model.pkl is loaded into the Flask application, ensuring quick predictions without retraining. A front-end interface is designed using HTML and CSS, where users can input their age, height, and weight to get a clothing size prediction. More pages then added to the web. 
   
# Installation
1. Clone or download the code
2. Make sure you already have the libraries installed
3. Activate environment by using `Scripts\activate`, make sure the cmd folder location is in the `Clothes-Size-Predictor\astyenv` folder
4. Use command `set FLASK_APP=main.py`
5. Use command `flask run`
