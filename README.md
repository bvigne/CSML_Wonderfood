# CSML

This is a CSML bot created to find recipes from Edamam's Recipe Search API with Startup plans.

## Installation

### Flows 
To build the entire bot, you have to create a new flow for each file in `flows` folder. A CSML flow name is equal to his flow filename.  Then copy/paste file content to the corresponding flow in the platform.

Default flow is `start.csml`.

### Functions
For each functions in `function` folder, build and install them with the following process.

#### append

To build the zip file, run this command:

```sh
cd functions/append/src
zip -g ../myzip.zip index.py
```

Import is made from the CSML platform in `functions` tab.

Click `add custom function` and fill the following parameters:

```sh
Upload a function : (click and select myzip.zip previously created)
Function name : "append"
Handler : "index.handler"
Runtime : "python3.6"
Arguments : "list" (list)
            "elem" (string)
            "unique" (bool)
Environment variables :
Description :
```
Click `Submit`, function would be created and can be used in CSML flows.

#### search_recipe

To build the zip file, run this command:

```bash
cd functions/search_recipe/src
pip install --target ./package -r requirements.txt
cd package
zip -r9 ../../myzip.zip .
cd ..
zip -g ../myzip.zip index.py
```

Import is made from the CSML platform in `functions` tab.

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

[CSML-platform](https://alpha.csml.dev)

[CSML-beta-access](http://bit.ly/csml-beta)

[CSML-documentation](https://docs.csml.dev)

[Edamam](https://developer.edamam.com/edamam-recipe-api)