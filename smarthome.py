import requests


def lightcontroll(onoff):
    if onoff == "True":
        print("Licht an")
    else:
        print("Licht aus")


def pccontroll(onoff):
    if onoff == "True":
        print("PC an")
    else:
        print("PC aus")


def storecontroll(onoff):
    if onoff == "rauf":
        requests.get("http://10.0.1.121:8087/set/hm-rega.0.4156.ProgramExecute?value=True")
    else:
        requests.get("http://10.0.1.121:8087/set/hm-rega.0.4168.ProgramExecute?value=True")


def storecontrollwh(onoff):
    if onoff == "rauf":
        print("Store rauf")
    else:
        print("Store runter")


def playmusic():
    pass


def playmusicwh():
    pass