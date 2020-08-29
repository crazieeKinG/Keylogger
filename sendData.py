import requests, json
import recordJSONManager as rJM


def sendData():
    recordsJson = rJM.readRecordLog()
    for key in recordsJson:
        if not recordsJson[key]:
            fname = key.split(".")[0]
            url = "https://api.jsonbin.io/b/"
            url2 = "https://api.jsonbin.io/b/5f4a160c4d8ce41113833b61"
            skey = "$2b$10$nGloURy4N0DelY2NloeBbOdFA5dvllnqgexGo0BVTtFzenqVhVTcC"
            headers = {
                "Content-Type": "application/json",
                "secret-key": skey,
                "name": "{0}".format(fname),
            }
            header2 = {
                "Content-Type": "application/json",
                "secret-key": skey,
                "versioning": "false",
            }
            header3 = {"secret-key": skey}
            dataToSend = rJM.readFile(key)
            try:
                req = requests.get(url2, headers=header3)
                linkdata = req.json()
                req = requests.post(url, json=dataToSend, headers=headers)
                bid = req.json()
                linkdata[fname] = bid["id"]
                requests.put(url2, json=linkdata, headers=header2)
                print("UPDATE TO SERVER {0} :: SUCCESS".format(key))
                recordsJson[key] = True
            except:
                print("CANNOT CONNECT TO SERVER :: {0} NOT UPLOADED".format(key))
    rJM.updateRecordLog(recordsJson)