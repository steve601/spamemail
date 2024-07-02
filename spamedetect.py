from flask import Flask,request,render_template
import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import numpy as np
import re

app = Flask(__name__)

model = load_model('C:/Users/odhia/OneDrive/Desktop/streamlit tut/email.keras')
tokenizer = pickle.load(open('emailtokenizer.pkl','rb'))

def preprocess_text(sentence):
    tag_pattern = re.compile(r'<.*?>')
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    # Lowercasing
    sent = sentence.lower()
    # Removal of HTML Tags
    sent = re.sub(tag_pattern, '', sent)
    # Removing Punctuation & Special Characters
    sent = re.sub('[^a-zA-Z]',' ',sent)
    # removing single character
    sent = re.sub(r"\s+[a-zA-Z]\s+",' ',sent)
    # removing multiple spaces
    sent = re.sub(r'\s+',' ',sent)
    # Removal of URLs
    sent = re.sub(url_pattern,'',sent)
    return sent

@app.route('/')
def homepage():
    return render_template('email.html')

@app.route('/classify',methods = ['POST','GET'])
def analyse_func():
    corpus = ""
    if request.method == 'POST':
        corpus = request.form.get('mail')
        inp = []
        inp.append(preprocess_text(corpus))
        inp = tokenizer.texts_to_sequences(inp)
        inp = pad_sequences(inp,padding='pre',maxlen = 100)
        
        pred = model.predict(inp)
        if pred > 0.5:
            msg = 'Spam email detected!!!'
        else:
            msg = "No spam email detected,Legit!!"
        
    return render_template('email.html', text=msg)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
    
    