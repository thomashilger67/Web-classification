import click
from scrap_site import scrap_data_from_website
import joblib
import pandas as pd
import pickle
import tensorflow as tf 
from tensorflow.keras.layers import TextVectorization
from tensorflow import keras
import numpy as np

def predict_nn(df_website, predict_proba):
    category = ['Arts', 'Business', 'Computers', 'Games', 'Health', 'Home', 'News',
       'Recreation', 'Reference', 'Science', 'Shopping', 'Society',
       'Sports']

    # Load the NN model
    nn_model = keras.models.load_model('model_pipeline/model_nn_glove')

    # Import the vectorizer
    vectorizer_data = pickle.load(open("model_pipeline/vectorizer_config_nn_glove.pkl", "rb"))
    vectorizer = TextVectorization.from_config(vectorizer_data['config'])
    # You have to call `adapt` with some dummy data (BUG in Keras)
    vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
    vectorizer.set_weights(vectorizer_data['weights'])

    # Vectorize the data
    X = []
    X.append(vectorizer(np.array(df_website.desc.values[0])).numpy())
    X=np.vstack(X)

    # Returns the probability category
    category_predicted_int = nn_model.predict(X)[0]

    if predict_proba:
        # Returns the probability for each category
        result_dict = dict(zip(category, category_predicted_int))
        return(result_dict)
    else :
        index, element = max(enumerate(category_predicted_int), key=lambda x: x[1])
        category_predicted = category[index]
        return(category_predicted)