#import nedded modules
import shutil
import os
#create a class MoveLogger 
class MoveLogger:
#log(src,dist) save a move to moves.log
    def log(self,source,distination):
        with open("moves.log","a+") as f:
            f.write(f"{source}->{distination}\n")
    def undo(self):
        try:
            with open("moves.log","r") as f:
                log = f.readlines()
                if  not log :
                    print("try to organize ur folder first!!")
                    return
                for line in reversed(log):
                    if "--session--" in line:
                        break
                    src , dest = line.strip().split("->")
                    shutil.move(dest,src)
        except FileNotFoundError :
            print("try to organize the folder first")
            print("you did not do  changes to undo them !!!!")
    def get_history(self):
        try: 
            with open("moves.log","r") as f:
                print("your history are:")
                for line in f:
                    if not line.strip():
                        print("no history found! try organize your folder first:)")
                        break
                    if "--session--" in line:
                        continue
                    _,dest = line.strip().split("->")
                    filename = os.path.basename(dest)
                    foldername = os.path.basename(os.path.dirname(dest))
                    print(f"+[{filename}] <<Was Moved To>> {foldername}/")
                    print("")
        except FileNotFoundError :
            print("you have no history yet try to organize your folder first:)")

