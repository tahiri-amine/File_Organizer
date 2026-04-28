#import nedded Modules 
import sys
from organiser import FileOrganiser
from logger import MoveLogger
l = sys.argv # [1] = the mode ; [2] = path; [0] = idk
#catch the mode and chose the correct function

logger = MoveLogger()
if len(l) < 2:
    print("Usage: py main.py <mode> [path] [args]")
    sys.exit()

if l[1] == "organize":
    organiser = FileOrganiser(l[2])
    organiser.organiser()
elif l[1] == "find":
    organiser = FileOrganiser(l[2])
    result = organiser.find_files(l[3])
    for file in result:
        print(file)
elif l[1] == "undo":
    logger.undo_last()
elif l[1] == "history":
    data = logger.get_history()
    if not data:
        print("No history yet.")
    else:
        print("__"*30, "your History:", "__"*30)
        for element in data:
            src, dist = element.split("->")
            print(f"{src} --------> {dist}")
else:
    print("Unknown mode. Check README.md")
    sys.exit()