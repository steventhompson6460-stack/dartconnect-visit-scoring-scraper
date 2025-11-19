import json

def load_json_file(path: str):
 with open(path, "r") as f:
 return json.load(f)

def load_text_lines(path: str):
 with open(path, "r") as f:
 return [x.strip() for x in f.readlines() if x.strip()]