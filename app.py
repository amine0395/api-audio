import json
import sys

from bson import json_util
from flask import Flask, request, jsonify
from pymongo import MongoClient
import gridfs

import data_retriever

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['snrt']
fs = gridfs.GridFS(db)
collection = db['snrt']

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to SNRT RESTful API</h1>"

@app.route('/fingerprint/<id>', methods=['GET'])
def fingerprint_data(id):
    return data_retriever.retrieve_data(id, fs)

@app.route('/waveform/<id>', methods=['GET'])
def waveform_data(id):
    return data_retriever.retrieve_data(id, fs)


@app.route('/info/<id>', methods=['GET'])
def info(id):
    id_str = int(id)
    document = collection.find_one({'﻿title_id': id_str})


    if document:
        document['_id'] = str(document['_id'])



        return jsonify({
                        "_id":document.get("_id"),
                        "title_id":document.get("﻿title_id"),
                        "title": document.get("title"),
                        "interpret": document.get("interpret"),
                        "author": document.get("author"),
                        "duration": document.get("duration"),
                        "Voice": document.get("Voice"),
                        "last_modif_time": document.get("last_modif_time"),
                        "is_online": document.get("is_online"),
                        "record_date": document.get("record_date"),
                        "soundfile_id": document.get("soundfile_id"),
                        "soundfile_name": document.get("soundfile_name"),
                        "keywords":document.get("keywords"),
                        "last_words":document.get("last_words")

                        })
    else:
        return jsonify({"error": "Data not found"}), 404
@app.route('/all', methods=['GET'])
def get_all_data():
    all_documents = list(collection.find())
    json_response = []
    for document in all_documents:
        json_response.append(json.loads(json_util.dumps(document)))
    return jsonify(json_response)

if __name__ == '__main__':
    app.run()
