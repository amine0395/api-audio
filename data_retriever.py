import json
from bson import ObjectId


def retrieve_data(waveform_id, fs):
    try:
        file_data = fs.get(ObjectId(waveform_id))
        waveform_json = json.loads(file_data.read().decode('utf-8'))
        return waveform_json
    except Exception as e:
        print(f"Error retrieving waveform data: {e}")



