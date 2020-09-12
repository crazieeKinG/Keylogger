# import requests, json
# import recordJSONManager as rJM


# def sendData():
#     url = "https://api.jsonbin.io/b/5f4b3aaa993a2e110d3969e7"
#     skey = "$2b$10$nGloURy4N0DelY2NloeBbOdFA5dvllnqgexGo0BVTtFzenqVhVTcC"
#     header1 = {
#         "Content-Type": "application/json",
#         "secret-key": skey,
#         "versioning": "false",
#     }
#     header2 = {"secret-key": skey}
#     recordsJson = rJM.readRecordLog()
#     count = 0
#     for key in recordsJson:
#         if not recordsJson[key]:
#             count += 1
#     try:
#         if count > 0:
#             req = requests.get(url, headers=header2)
#             linkdata = req.json()
#             for key in recordsJson:
#                 if not recordsJson[key]:
#                     fname = key.split(".")[0]
#                     dataToSend = rJM.readFile(key)
#                     try:
#                         linkdata[fname] = dataToSend
#                         requests.put(url, json=linkdata, headers=header1)
#                         print("UPDATE TO SERVER {0} :: SUCCESS".format(key))
#                         recordsJson[key] = True
#                     except:
#                         print(
#                             "CANNOT CONNECT TO SERVER :: {0} NOT UPLOADED".format(key)
#                         )
#             rJM.updateRecordLog(recordsJson)
#     except:
#         print("CANNOT CONNECT TO SERVER :: NOT UPLOADED")