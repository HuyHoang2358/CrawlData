import requests
import json
import os
URL = "https://api-app.map4d.vn/map/object/"
SAVE_FOLDER_PATH = "data/"
OBJECT_ID_FILE = "object_id.txt"
logs = []

def get_data_by_id(object_id):
    try:
        main_url = URL + object_id
        response = requests.get(main_url)
        with open(SAVE_FOLDER_PATH + object_id + '.json', 'w') as f:
            json.dump(json.loads(response.text), f, indent=4)
        
        city_object = json.loads(response.text)["result"]

        model = city_object["model"]
        objUrl = model["objUrl"]
        objImg = model["textureUrl"]

        response = requests.get(objUrl)
        open(SAVE_FOLDER_PATH + object_id +".obj", "wb").write(response.content)

        response = requests.get(objImg)
        open(SAVE_FOLDER_PATH + object_id +".png", "wb").write(response.content)
        logs.append("DONE__" + object_id + "\n")
    except Exception as e:
        logs.append("ERROR_" + object_id + "\n")
        logs.append(e)

def init():
    if os.path.exists(SAVE_FOLDER_PATH) == False:
        os.mkdir(SAVE_FOLDER_PATH)
        print(f"Created {SAVE_FOLDER_PATH}")


def main():
    object_id = []
    with open(OBJECT_ID_FILE, 'r') as f:
        lines = f.readlines()
    for line in lines[:1]:
        object_id.append(line[:-1])
    
    print(f"Total line in object_id.txt file: {len(object_id)}")

    # check unique value
    objectID_unique = set(object_id)
    print(f"Total object: {len(objectID_unique)}")

    print(f"Strating download all model by ID --------------------------------")
    print(f"----  All data will save in data/ folder")
    print(f"----  With each object ID we will save 3 files - .obj, .json, .png")
    print(f"----  .obj save shape model")
    print(f"----  .json save all static information of model")
    print(f"----  .png save all texture ")

    for id in objectID_unique:
        get_data_by_id(id)
        

    with open('logs.json', 'w') as f:
        json.dump(logs, f)


# --------------------------------------------------------------------MAIN ----------------------------
init()
main()

