import configparser
import os

def loadSettings():
    path_Settings = "Settings.ini"
    settings = configparser.ConfigParser()
    settings.optionxform = str
    if not os.path.exists("./" + path_Settings):  # iniファイルが存在していないとき
        settings["default"] = \
            {
                "eventColor": "#00ff00",
                "feverColor": "#fa8072"
            }
        with open(path_Settings, "w", encoding="utf-8") as newSettings:
            settings.write(newSettings)

    settings.read("./" + path_Settings, 'UTF-8')
    localSettings = dict(settings["default"])

    return localSettings

def localSettings():
    return