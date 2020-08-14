if pygame.mouse.get_pressed()[0]:
    data["mouseHold"] += 1
else:
    data["mouseHold"] = 0

for i in range(len(data["widgetcode"])):
    try:
        data["keycache"] = list(data["widgetcode"].keys())[i]
        widget = data["var"][data["keycache"]].copy()
        exec(data["widgetcode"][data["keycache"]])
        data["var"][data["keycache"]] = widget.copy()
        
        screen.blit(widget["surface"], [widget["x"], widget["y"]])
    except Exception as e:
        holo.new_alert(SYSTEM_TEXTS["widget_crash"].replace("__WIDGET__", data["keycache"]) + str(e))
        #TODO: MEMDUMP DES WIDGETS IN DIE LOGS SCHREIBEN
        del data["var"][data["keycache"]]
        del data["widgetcode"][data["keycache"]]
        del data["eventcode"][data["keycache"]]
        data["widgetfile"][data["keycache"]]["enabled"] = 0
        with open(holo.path("USERS/WIDGETS"), "w") as f:
            f.write(str(data["widgetfile"]))
            f.close()

try:
    if pygame.mouse.get_pressed()[0] and data["mouseHold"] >= 6:
        data["mousePos"] = list(pygame.mouse.get_pos())
        if data["mouseHold"] == 6:
            for i in data["var"].keys():
                if (data["mousePos"][0] in range(data["var"][i]["x"], data["var"][i]["x"] + data["var"][i]["size"][0])) and (data["mousePos"][1] in range(data["var"][i]["y"], data["var"][i]["y"] + data["var"][i]["size"][1])):
                    data["moveObjectName"] = i
                    break
        else:
            data["var"][data["moveObjectName"]]["x"] = data["mousePos"][0] - (data["var"][data["moveObjectName"]]["size"][0] // 2)
            data["var"][data["moveObjectName"]]["y"] = data["mousePos"][1] - (data["var"][data["moveObjectName"]]["size"][1] // 2)
            
    else:
        data["moveObjectName"] = ""
except:
    pass


#OVERLAY
screen.blit(data["assets"]["overlaySurface"], [0, SETTINGS["height"] - data["assets"]["overlaySurface"].get_height()])
screen.blit(data["assets"]["home"], [SETTINGS["width"] // 2 - data["assets"]["home"].get_width() // 2, SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
screen.blit(data["assets"]["add"], [int(SETTINGS["width"]*0.01), SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
screen.blit(data["assets"]["delete"], [SETTINGS["width"] - data["assets"]["home"].get_width(), SETTINGS["height"] // 20 - data["assets"]["home"].get_height() // 2 + int(SETTINGS["height"]*0.9)])
