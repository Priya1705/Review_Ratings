# def pipeline_load():
#     from transformers import pipeline
#     classifier = pipeline('sentiment-analysis')

def review_sentiment(file):
    # x="helloooo"
    # print(x)
    # return x
#     classifier = classify

    import pandas as pd
    import numpy as np
    import re

    from transformers import pipeline
    classifier = pipeline('sentiment-analysis')
    
    dataset = pd.read_csv(file)
    data=pd.DataFrame(list(zip(dataset["Text"], dataset["Star"])),columns=['Text','Star'])
    
    a = data.isnull().sum()
    a = a.sum()
    if a>0:
        data=data.dropna()
        data = data.reset_index(drop=True)
        
    def clean(text):
        # text = re.sub('[^A-Za-z]+', ' ', text)
        return text.lower()
    data['CleanedText'] = data['Text'].apply(clean)
    
    
    
    value=[]
    def get_sentiment(blue):
        text = data["CleanedText"]
        for i in range(0, len(data)):
            x = classifier(text[i])
            label = x[0]['label']
            if label == 'POSITIVE' :
                value.append(1)
            elif label == 'NEGATIVE' :
                value.append(-1)
            else :
                value.append(0)    
    get_sentiment(data)
    data["value"]=value
    
    variant_star=[]
    variant_text=[]
    
    def identify(star,value,text):
        for i in range(0,len(data)):
            if star[i]==1 or star[i]==2 :
                if value[i] == 1.0 :
                    variant_star.append(star[i])
                    variant_text.append(text[i])

    identify(data["Star"],data["value"],data["Text"])
    df=pd.DataFrame(list(zip(variant_star, variant_text)),columns=['Star','Text'])
    
# #     # ls=[1,2,3]
# #     # lt=[5,6,7]
# #     # df=pd.DataFrame(list(zip(ls,lt)))
# #     # import pickle
# #     # pickled = pickle.dumps(df)
# #     # import base64
# #     # pickled_b64 = base64.b64encode(pickled)
# #     # # pickled_b64
# #     # hug_pickled_str = pickled_b64.decode('utf-8')
# #     # # hug_pickled

    df = df.to_json()

    return df

    # print(df)
    
# file ='chrome_reviews.csv'
# review_sentiment(file)