import json

from dados import produto

with open('Json_teste.json', 'w+') as file:
    dict_json = json.dumps(produto, indent=True)
    file.write(dict_json)
    file.seek(0)
    readable_json = file.read()
    print(readable_json)

with open('Json_teste.json', 'r') as file:
    json_file = file.read()
    json_to_dict_file = json.loads(json_file)
    print(json_to_dict_file)
