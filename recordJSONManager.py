# List of all characters
character_list = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','TAB','CAPS_LOCK','SHIFT','CTRL_L','CMD','ALT_L','ALT_R','MENU','CTRL_R','SHIFT_R','ENTER','BACKSPACE','PRINT_SCREEN','SCROLL_LOCK','PAUSE','INSERT','HOME','PAGE_UP','DELETE','END','PAGE_DOWN','UP','DOWN','LEFT','RIGHT','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"','>','?','<','~','`','-','=','[',']','\\',';','""',',','.','/','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']
length = len(character_list)
# Dependencies
import json
# Function to create file
def createFile(username:str,latest_date:str,old_date:str):
    global character_list
    file_data = dict()
    file_data['username'] = username
    file_data['recordedDate'] = latest_date
    file_data['characters'] = list()
    for char in character_list:
        temp = {'ch':char,'count':0}
        file_data['characters'].append(temp)
    # print(file_data)
    with open('records/{0}-{1}.json'.format(username,latest_date),"w") as rfile:
        rfile.write(json.dumps(file_data))
        rfile.close()
    if old_date != "LATEST DATE":
        addRecordLog('{0}-{1}.json'.format(username,old_date))
# Function to read record file
def readFile(filename:str):
    file_data = dict()
    with open('records/{0}'.format(filename),"r") as rf:
        file_data = json.load(rf)
        rf.close()
    return file_data
# Function to update file
def updateFile(username:str,latest_date:str,keys:list):
    global character_list,length
    file_data = readFile('{0}-{1}.json'.format(username,latest_date))
    for chars in keys:
        # print(chars)
        for i in range(length):
            if file_data['characters'][i]['ch'] == chars:
                file_data['characters'][i]['count'] += 1 
    with open('records/{0}-{1}.json'.format(username,latest_date),"w") as rfile:
        rfile.write(json.dumps(file_data))
# Function to read record log file
def readRecordLog():
    with open('records.json','r') as lfile:
        logdata = json.load(lfile)
        lfile.close()
    return logdata
# Function to add record log file
def addRecordLog(recordFile:str):
    logJson = readRecordLog()
    logJson[recordFile] = False
    with open('records.json','w') as lfile:
        lfile.write(json.dumps(logJson))
        lfile.close()
# Function to update record log file
def updateRecordLog(recordFile:dict):
    with open('records.json','w') as lfile:
        lfile.write(json.dumps(recordFile))
        lfile.close()
