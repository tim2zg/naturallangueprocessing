import smarthome


def dooer(location, was, wann, wie):
    if wann == "":
        pass
    else:
        print("Zeit noch nicht Implementiert")
    if location == "l-tim":
        if was == "licht":
            smarthome.lightcontroll(wie)
        elif was == "PC":
            smarthome.pccontroll(wie)
        elif was == "store":
            smarthome.storecontroll(wie)

    elif location == "l-wohnzimmer":
        if was == "store":
            smarthome.storecontrollwh(wie)


def spieler(location):
    if location == "l-tim":
        smarthome.playmusic()
    elif location == "l-wohnzimmer":
        smarthome.playmusicwh()