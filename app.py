from flask import Flask, request
import pickle
import pandas as pd
# import flasgger
import os
from rating_reviews import review_sentiment
# from flasgger import Swagger
from flask import Flask, render_template, request
import base64
import json

from werkzeug.utils import secure_filename

from transformers import pipeline

# from werkzeug.datastructures import  FileStorage

# project_root = os.path.dirname(__file__)
# template_folder=os.path.join(project_root, './template/')

app=Flask(__name__)
# Swagger(app)

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

# classifier = pipeline_load()
classifier = pipeline('sentiment-analysis')
# @app.route('/')
# def welcome():
#     return "Welcome All"

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/file_upload', methods=['POST'])
def file_handler():
    f = request.files['file']
    # f.save(secure_filename(f.filename))
    y = review_sentiment(f.filename, classifier)
    data = json.loads(y)
    df = pd.DataFrame.from_records(data)

    x = df.iloc[:,:]

    return render_template('view.html',tables=[x.to_html(classes='x')],
    titles = ['na', 'Table'])
    # return m

if __name__=='__main__':
    # app.run(host='0.0.0.0',port=8000)
    app.run()
    
    



    
#     ss_df = pickle.loads(base64.b64decode(hug_pickled.encode())
# >>> ss_df