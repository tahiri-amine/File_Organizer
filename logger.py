#import nedded modules
import shutil
import os
#create a class MoveLogger ; the class should take 3 mehods
class MoveLogger:
#log(src,dist) save a move to moves.log
    def log(self,source,distination):
        with open("moves.log","a+") as f:
            f.write(f"{source}->{distination}\n")
#undo last(self) that read the last move and reverse it
    def undo_last(self):
        with open("moves.log","r") as f:
            logs = f.readlines()
            if not logs:
                print("there is nothing to undo")
                return
            log = logs[-1].strip()
            src,dist = log.split("->")
            shutil.move(dist,src)
#and the get history methode that return all the history inside the file as a list
#oh i overthinged about it no need for seek jsut open thte file in r mode and the cursor will point on the begging of the file
    def get_history(self):
        with open("moves.log","r") as f:
            data = f.readlines()
            if not data:
                return None
            return data
            #return   [element.strip() for element in data]