import json

def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        return {"raw": text}
