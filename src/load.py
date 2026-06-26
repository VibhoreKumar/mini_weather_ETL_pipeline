import json

def append_record(record, path):
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")