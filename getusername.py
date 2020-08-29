import settingsManager as sM
uname = ""
while uname == "":
    uname = input('Set your username: ')
    print(uname)
sM.setUsername(uname)