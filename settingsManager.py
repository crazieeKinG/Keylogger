import json

# Function to read content of settings.json file
def readSetting():
    json_data = dict()
    with open("settings.json", "r") as sfile:
        json_data = json.load(sfile)
        sfile.close()
    return json_data


# Function to set up username
def setUsername(username: str):
    prev_data = readSetting()
    prev_data["username"] = username
    with open("settings.json", "w") as sfile:
        sfile.write(json.dumps(prev_data))
        sfile.close()


# Function to set up latest_date
def setLatestDate(latest_date: str):
    prev_data = readSetting()
    prev_data["Latest_record_date"] = latest_date
    with open("settings.json", "w") as sfile:
        sfile.write(json.dumps(prev_data))
        sfile.close()


def setVersion(version:str):
    prev_data = readSetting()
    prev_data["version"] = version
    with open("settings.json", "w") as sfile:
        sfile.write(json.dumps(prev_data))
        sfile.close()