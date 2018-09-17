from flask import Flask,request,render_template,jsonify

from sanitization import sanitization

app=Flask(__name__)


import pandas as pd
import numpy as np
import random
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def predict(l):
    

    file = "pickel_model.pkl"
    with open(file, 'rb') as f1:  
        lgr = pickle.load(f1)
    f1.close()
    
    
    file = "pickel_vector.pkl"
    with open(file, 'rb') as f2:  
        vectorizer = pickle.load(f2)
    f2.close()


    x_predict = [l]
    
    x_predict = vectorizer.transform(x_predict)
    y_predict = lgr.predict(x_predict)
    
    print (y_predict)
        
    return y_predict



@app.route('/')
def home():
    return render_template('index1.html')
    
@app.route('/request',methods=['POST'])
def call():
    
    x= request.form['url']
    o=predict(x)
    
    if(o[0] == 'good'):
        return render_template('safe.html',var = x)
    
    if(o[0] == 'bad'):
        return render_template('danger.html',var = x)




app.run(port=8060)