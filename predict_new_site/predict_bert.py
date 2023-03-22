from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scrap_site import scrap_data_from_website
import torch

def predict_bert(data, predict_proba):
    tokenizer = AutoTokenizer.from_pretrained("alimazhar-110/website_classification")
    model = AutoModelForSequenceClassification.from_pretrained("alimazhar-110/website_classification")

    inputs = tokenizer(data[:500], return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    probabilities = torch.nn.functional.softmax(logits, dim=1)

    if predict_proba:
        # Returns the probability for each category
        probabilities = probabilities.tolist()[0]
        categories = list(model.config.id2label.values())
        result_dict = dict(zip(categories, probabilities))
        return(result_dict)
    else :
        # Returns the predicted category
        predicted_class_id = logits.argmax().item()
        category_predicted= model.config.id2label[predicted_class_id]
        return(category_predicted)
