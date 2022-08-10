import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class SizePrediction():
    #training function, runs only once when user open the Size Predictor page
    def training(self):
        #read csv file
        df = pd.read_csv("clothes_size.csv")

        #drop null values
        df = df.dropna()

        #change label
        global encode
        encode = {"size":{"XXS": 0, "XS": 1, "S":2, "M":3, "L":4, "XL":5, "XXL":6, "XXXL":7}}
        df = df.replace(encode)

        #split data, X (age, weight, height) is features, y is label
        X = df.iloc[:,:-1]
        y = df['size']
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)
        
        #defining model
        global rf_model 
        rf_model = RandomForestClassifier()

        #fitting train data
        rf_model.fit(X_train,y_train)

        #predicting test data
        y_rf_pred = rf_model.predict(X_test)
        # print(accuracy_score(y_test,y_rf_pred))

    #predict function, runs whenever user click 'Predict' button
    def predict(self, age, height, weight):
        #assigning parameters into dictionary
        d = {'weight':[weight], 'age': [age], 'height': [height]}

        #make dataframe from d dictionary
        user_data = pd.DataFrame(data=d)

        #predict input from user
        pred_res = rf_model.predict(user_data)[0]

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

#bagian ini dimasukkan ke fungsi untuk menampilkan halaman Clothes Size Prediction
SP = SizePrediction()
SP.training()
prediction_result = SP.predict(22,170,69)
#----------------------------------------------------------------------------------