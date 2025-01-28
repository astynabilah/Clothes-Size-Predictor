import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from wtforms import validators
from wtforms import SelectField, SubmitField, StringField
from flask_wtf import FlaskForm

class SizePrediction:
    def __init__(self):
        self.model_file = "size_model.pkl"  # File pickle model
        self.encode = {"size": {"XXS": 0, "XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5, "XXL": 6, "XXXL": 7}}
        self.model = self.load_model()  # Load model saat aplikasi Flask dimulai

    def load_model(self):
        """Load model dari pickle file, tanpa training ulang."""
        if os.path.exists(self.model_file):
            with open(self.model_file, "rb") as file:
                print("Model loaded successfully from pickle file.")
                return pickle.load(file)
        else:
            print("Model file not found! Please run 'train_model.py' first.")
            return None
        
    #predict function, runs whenever user click 'Predict' button
    def predict(self, age, height, weight):

        if self.model is None:
            return "Model not available. Please run 'train_model.py' first."
        
        #assigning parameters into dictionary
        d = {'weight':[weight], 'age': [age], 'height': [height]}

        #make dataframe from d dictionary
        user_data = pd.DataFrame(data=d)

        #predict input from user
        pred_res = self.model.predict(user_data)[0]

        #return prediction result to be displayed on web using Flask
        if pred_res == 0:
            return "XXS"
        elif pred_res == 1:
            return "XS"
        elif pred_res == 2:
            return "S"
        elif pred_res == 3:
            return "M"
        elif pred_res == 4:
            return "L"
        elif pred_res == 5:
            return "XL"
        elif pred_res == 6:
            return "XXL"
        elif pred_res == 7:
            return "XXXL"

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/sizepred',methods=['GET', 'POST'])
def size():
    global pred
    pred = ""
    SP = SizePrediction()
    # SP.training()
    if request.method == 'POST':
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        pred = SP.predict(float(age), float(height), float(weight))
        print(pred)
        return render_template('sizepred.html',pred_text=pred)
    return render_template('sizepred.html',pred_text=pred)

@app.route('/colorcalc', methods=['GET','POST'])
def color():
    #pilihan warna yang ada, untuk bagian <select> di html
    colors = ['','Pink','Red','Orange','Beige','Yellow','Green','Light Blue','Dark Blue','Purple','Brown','Grey']
    
    #img_src dan selected_color dibuat kosong, untuk dipakai di if condition di file html
    img_src= ''
    selected_color = ''

    #post form yang berisi dropdown dan button
    if request.method == 'POST':
        #get warna yang dipilih user
        selected_color = request.form.get('selected_color')
        
        if selected_color!='': #jika user sudah memilih warna
            #url gambar yang dipilih user
            color_img = 'images/colors/'+str(selected_color).lower()+'.png'
            color_img = color_img.replace(' ','_') #menghilangkan spasi yang ada di Light Blue dan Dark Blue (sesuai nama file gambarnya juga)
            
            #url gambar pasangan warna
            img_src = 'images/colors/'+str(selected_color).lower()+'-pair.png'
            img_src = img_src.replace(' ','_') #menghilangkan spasi yang ada di Light Blue dan Dark Blue (sesuai nama file gambarnya juga)
            return render_template('colorcalc.html',colors=colors, img_src=img_src, sc = selected_color, color_img=color_img)
    return render_template('colorcalc.html',colors=colors, img_src=img_src)

@app.route('/skintone',methods=['GET','POST'])
def skin():
    #pilihan warna yang ada, untuk bagian <select> di html
    skin = ['','Fair','Warm','Beige','Honey','Brown','Dark']
    
    #img_src dan selected_color dibuat kosong, untuk dipakai di if condition di file html
    img_src= ''
    selected_skin = ''

    #post form yang berisi dropdown dan button
    if request.method == 'POST':
        #get warna kulit yang dipilih user
        selected_skin = request.form.get('selected_skin')
        
        if selected_skin!='': #jika user sudah memilih warna
            #url gambar pasangan warna
            img_src = 'images/skin/'+str(selected_skin).lower()+'-pair.jpeg'

            return render_template('skin.html',skin=skin, img_src=img_src, sk = selected_skin)
    return render_template('skin.html',skin=skin, img_src=img_src)
