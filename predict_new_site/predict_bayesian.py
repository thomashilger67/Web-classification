import joblib

def predict_bayesian(df_website, predict_proba):
    # Categories of the bayesian model
    category = ['Arts', 'Business', 'Computers', 'Games', 'Health', 'Home', 'News',
       'Recreation', 'Reference', 'Science', 'Shopping', 'Society',
       'Sports']
    
    # Load the Bayesian model
    loaded_model = joblib.load('model_pipeline/pipeline_nb.pkl')


    if predict_proba:
        # Returns the probability for each category
        category_predicted_int = loaded_model.predict_proba(df_website.desc.values)
        result_dict = dict(zip(category, category_predicted_int[0]))
        return(result_dict)
    else :
        # Returns the predicted category
        category_predicted_int = loaded_model.predict(df_website.desc.values)
        category_predicted = category[category_predicted_int[0]]
        return(category_predicted)