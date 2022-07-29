from flask import Flask,render_template,request

import joblib

# load the model
model = joblib.load('predict_79.pkl')


# initialise the app
app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('home.html')

@app.route('/forms')
def forms():
    return render_template("forms.html")

@app.route('/predict', methods=['post'])
def predict():
    # names=['preg','plas','pres','skin','test','mass','pedi','age','class']

    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    data = model.predict([[preg,plas,pres,skin,test,mass,pedi,age ]])

    if data[0] == 0:
        resp ='not diabitic'
    else:
        resp = 'diabitic'
    
    return render_template('forms.html', data=resp)



app.run(debug = True)