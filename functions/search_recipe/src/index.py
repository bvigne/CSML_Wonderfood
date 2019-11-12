import os
import requests


def handler(event, context):

    if "q" not in event:
        return {"error": "Exactly one of these `q` or `r` fields must be present."}

    base_url = "https://api.edamam.com/search?"
    app_id = os.environ.get('edamam_id')
    app_key = os.environ.get('edamam_key')
    query = f"{base_url}q={event['q']}&app_id={app_id}&app_key={app_key}"

    if "from" in event and event["from"]:
        query = f"{query}&from={event['from']}"
    if "to" in event and event["to"]:
        query = f"{query}&to={event['to']}"
    if "ingr" in event and event["ingr"]:
        query = f"{query}&ingr={event['ingr']}"
    if "diet" in event and len(event["diet"]) > 0:
        query = f"{query}&diet={event['diet'][0]}"
    if "health" in event and len(event["health"]) > 0:
        query = f"{query}&health={'&health='.join(filter(None, event['health']))}"
    if "cuisineType" in event and len(event["cuisineType"]) > 0:
        query = f"{query}&cuisineType={'&cuisineType='.join(filter(None, event['cuisineType']))}"
    if "mealType" in event and len(event["mealType"]) > 0:
        query = f"{query}&mealType={event['mealType'][0]}"
    if "dishType" in event and len(event["dishType"]) > 0:
        query = f"{query}&dishType={'&dishType='.join(filter(None, event['dishType']))}"
    if "calories" in event and event["calories"]:
        query = f"{query}&calories={event['calories']}"
    if "time" in event and event["time"]:
        query = f"{query}&time={event['time']}"
    if "excluded" in event:
        query = f"{query}&excluded={'&excluded='.join(filter(None, event['excluded']))}"

    response = requests.get(query)
    if response.status_code == 200:
        json = response.json()
        return json
    else:
        return {"error": f"Status code {response.status_code}."}
