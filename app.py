# from models import sentiment, political
from utils import retrieve, write
from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/query', methods=['POST'])
def query():
    # extract query from request and read from database
    query_id = request.get_json()["query_id"]
    # query_data = retrieve.fetch(query_id)

    # run models on query data
    # sentiment_results = sentiment.run(query_data)
    # political_results = political.run(query_data)

    # store results
    write.store(query_id)

    return jsonify(query_id)

def political(data):
  pass

