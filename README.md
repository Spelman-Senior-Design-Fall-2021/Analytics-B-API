# Analytics B API

This is the source for a webservice than can be called to run Analytics B's models. It utilizes Flask for the server. The models are written using nltk's VADER sentiment model and a tensorflow keras political bias model. The PB model is based on work from https://github.com/DylanModesitt/political-sentiment. 

Live API: https://analytics-b-api-kxgii.ondigitalocean.app

Firebase store: https://analytics-b-api-default-rtdb.firebaseio.com/query or https://analytics-b-api-default-rtdb.firebaseio.com/query/<query_id>.json

### Endpoints

#### /query
Accepts an HTTP POST request with JSON mapping a **query_id** to a value generated by webscraping as well as an array named **data** of dictionaries holding **url** and **clean_text** maps. The service then runs the machine learning models, writes the results to Firebase and returns them as JSON in the response body. 

- See example_request.json for example input (consider changing query id to new UUID for testing)
- Utilize https://reqbin.com for mocking requests



### Development
- Work on branch then execute PR to merge in changes
- Server can be tested locally with ***flask run***
- Pushes or merges into main are deployed on Digital Ocean automatically