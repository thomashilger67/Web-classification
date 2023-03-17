# Website classification

Github repository for the end-of-the-year project with IMATAG at ENSAI. The goal of this project is to add information to Imatag's data. Our main focus was to classif all the website in the dataset.

### How to use

You can try to categorize a website using the following command :

```cmd
python3 main.py --website_url <<insert_an_url_here>> --predict_proba <<True or False>>
```

This command will return the predicted category for the website. 

If `--predict_proba` is set to False it only return the category predicted. If it is set to `True` it returns the probability for all the categories.

You can also select the model you want to use using the `--model` parameter (not working yet).

Here are some examples (with a naive bayesian model) :

```cmd
> python3 main.py --website_url https://www.bbc.com/news
> Society
> python3 main.py --website_url https://www.leparisien.fr/
> Recreation
> python3 main.py --website_url https://www.apple.com/fr/
> Computers
```