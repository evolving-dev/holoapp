os.chdir(PATH)

with open(os.path.join(PATH,"INITFILE"),"r") as f:
    INITFILE = f.readlines()
    f.close()

os.mkdir("USERS")
os.chdir(os.path.join(PATH,"USERS"))

SETTINGS = {
    "width":int(INITFILE[0]),
    "height":int(INITFILE[1]),
    "lang":"en-US",
    'background':'standard.png',
    'theme':'dark',
    'timeout':120,
    'keyboard':'qwerty',
    'timeformat': '%H:%M:%S',
    'dateformat':'%d.%m.%Y'
    }

with open("settings","w") as f:
    f.write(str(SETTINGS))
    f.close()

os.chdir(PATH)
os.remove("INITFILE")
#CREATING USER DIRECTORY AND WRITING SETTINGS FILE TO IT

exec(readfile(os.path.join(PATH,"scripts/init/HOLO_START.py")),globals())