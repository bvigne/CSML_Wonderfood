# CSML

This is a CSML bot created to find recipes from Edamam's Recipe Search API with Startup plans.

## Installation

You can upload this bot on https://studio.csml.dev.
In order to do so, clone this repo, import the file `wonderfood.zip`.


## Functions

#### search_recipe

Functions are automatically added to your newly imported chatbot, you only need to add environment variables.
Yet you might want to edit functions.
To upload a modified function, build the zip file, run this command:

```bash
cd functions/search_recipe/src
pip install --target ./package -r requirements.txt
cd package
zip -r9 ../../myzip.zip .
cd ..
zip -g ../myzip.zip index.py
```

Click `add custom function` and fill the following parameters:

```sh
Upload a function : (click and select myzip.zip previously created)
Function name : "search_recipe"
Handler : "index.handler"
Runtime : "python3.6"
Arguments : "q" (string)
            "from" (number)
            "to" (number)
            "ingr" (string)
            "diet" (list)
            "health" (list)
            "cuisineType" (list)
            "mealType" (list)
            "dishType" (list)
            "calories" (string)
            "time" (string)
            "excluded" (list)
Environment variables : "edamam_id" (Edamam API account id)
                        "edamam_key" (Edamam API account key)
Description :
```
Click `Submit`, function would be created and can be used in CSML flows.

## Links
[Clevy](https://clevy.io/)

[CSML-platform](https://studio.csml.dev)

[CSML-beta-access](http://bit.ly/csml-beta)

[CSML-documentation](https://docs.csml.dev)

[Edamam](https://developer.edamam.com/edamam-recipe-api)
