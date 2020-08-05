#UPDATE CODE: Runs once every frame

#Create necessary texts
widget["date"] = time.strftime(SETTINGS["dateformat"])
widget["time"] = time.strftime(SETTINGS["timeformat"])
widget["weekday"] = SYSTEM_TEXTS["weekdays"][int(time.strftime("%w"))]

#If the texts are not the same
if not (widget["date"] == widget["texts_old"][0] and widget["time"] == widget["texts_old"][1]):
    
    #Create widget surface
    widget["surface"] = pygame.Surface([SETTINGS["width"] // 5, SETTINGS["width"] // 10], pygame.SRCALPHA)

    #Render the texts
    widget["date_surface"] = FONTS["p-sans-serif"].render(widget["weekday"] + ", " + widget["date"], True, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0])
    widget["time_surface"] = FONTS["h4"].render(widget["time"], True, [255,255,255] if SETTINGS["theme"] == "dark" else [0,0,0])

    #Blit the texts onto the widget surface
    widget["surface"].blit(widget["date_surface"], [SETTINGS["width"] // 10 - widget["date_surface"].get_width() // 2,0])
    widget["surface"].blit(widget["time_surface"], [SETTINGS["width"] // 10 - widget["time_surface"].get_width() // 2,widget["date_surface"].get_height()])


widget["texts_old"] = [widget["date"], widget["time"]]