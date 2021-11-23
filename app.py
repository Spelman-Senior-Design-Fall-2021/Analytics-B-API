from models import sentiment  # , political
from firebase_admin import delete_app
from utils import write
from flask import Flask, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/query', methods=['POST'])
def query():
    try:
        # extract query from request
        query = request.get_json()
        query_id = query["query_id"]
        query_data = query["data"]

        # run models on query data
        results = run_models(query_id, query_data)

        # store results
        write.store(query_id, results)
        return jsonify(results)
    except Exception as e:
        error = {"error_message": str(e)}
        return jsonify(error)


def run_models(id, data):
    
    # result info
    results = {"query_id": id,
               "sentiment": [],
               "political": []
               }
    
    # run models
    for d in data:
      text = d["clean_text"]
      url = d["url"]
      results["sentiment"].append({"url": url})
      results["sentiment"].append(sentiment.run(text))
      # results["political"] = political.run(text)

    return results
