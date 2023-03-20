from flask import Flask,render_template,request,redirect
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
model=pickle.load(open("modelf.pkl","rb"))
model1=pickle.load(open("model2.pkl","rb"))

app=Flask(__name__,)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_species():

    sepal_length=float(request.form.get("sepal_length"))
    sepal_width=float(request.form.get("sepal_width"))
    petal_length=float(request.form.get("petal_length"))
    petal_width=float(request.form.get("petal_width"))
    
    
    result=model.predict(np.array([[sepal_length,sepal_width,petal_length,petal_width]]))
    
    if result[0]=="setosa":
        return "<h1 style='color:green'>Setosa</h1>"
    else:
        return "<h1 style='color:red'>Versicolor</h1>"
@app.route("/predicts",methods=["POST"])
def predict_species1():

    sepal_length=float(request.form.get("sepal_length"))
    sepal_width=float(request.form.get("sepal_width"))
    petal_length=float(request.form.get("petal_length"))
    petal_width=float(request.form.get("petal_width"))
    
    
    result1=model1.predict(np.array([[sepal_length,sepal_width,petal_length,petal_width]]))
    
    if result1[0]==0:
        return "<h1 style='color:green'>Setosa</h1>"
    elif result1[0]==1:
        return "<h1 style='color:red'>versicolor</h1>"   
    
  

app.run(debug=True,port=5001)