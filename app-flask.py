from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open('maas.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tecrube=float(request.form.get('tecrube'))
    yazili=float(request.form.get('yazili'))
    mulakat=float(request.form.get('mulakat'))
    tahmin=model.predict([[tecrube,yazili,mulakat]])
    return render_template('index.html', tahmin='Yapay zeka tarafından tahmin edilen gelirini: ${}'.format(tahmin))


if __name__=='__main__':
    app.run(debug=True)