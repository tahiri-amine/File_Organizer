#imoport nedded modules
import os
import shutil
from logger import MoveLogger
#create a class that named FileOrganiser
class FileOrganiser:
#the constractor must take the path as the paramertre and check if that path exist
    def __init__(self,path):
        self.logger = MoveLogger()
        if os.path.exists(path) :
            self.path = path
        else:
            raise ValueError("Path not found! ")
    
   
#a methode organiser that move each file into a subfolde named with the file extention
    def organiser(self):
        self.logger.log("--session--","--session--")
        files = os.listdir(self.path)
        for file in files:
            if os.path.isfile(os.path.join(self.path,file)):
                _,ext = os.path.splitext(file)
                sub_folder = os.path.join(self.path,ext[1:])
                os.makedirs(sub_folder,exist_ok=True)
                self.logger.log(os.path.join(self.path,file),os.path.join(sub_folder, file))
                shutil.move(os.path.join(self.path,file),sub_folder)
            else:
                continue
#a find methode that takes an ext and return all files with that extention
    def find_files(self,ext,path = None):#this one must check subfolders too
        if not ext.lower().startswith("."):
                    ext = "." + ext
        founded_files = []
        if path is None:
            path = self.path
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(os.path.join(path,file)):
                _,extention = os.path.splitext(file)
               
                if ext.lower() == extention:
                    founded_files.append(file)
                else:
                   continue
            else:
                founded_files.extend(self.find_files(ext,os.path.join(path,file)))
        return founded_files
    def preview(self):
            print("Preview Mode:")
            files = os.listdir(self.path)
            for file in files:
                if os.path.isfile(os.path.join(self.path,file)):
                    _,ext = os.path.splitext(file)
                    print(f"+[{file}] <<-- Will Be Moved To -->> {ext[1:]}/\n")
    


                

