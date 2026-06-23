import argparse
from organiser import FileOrganiser 
from logger import MoveLogger
parser = argparse.ArgumentParser(description="File Organizer")
sub_parser = parser.add_subparsers(dest ="command")
organize = sub_parser.add_parser("organize")
find = sub_parser.add_parser("find")
undo = sub_parser.add_parser("undo")
history = sub_parser.add_parser("history")
organize.add_argument("-fp","--folder_path",required=True)
find.add_argument("-fp","--folder_path",required=True)
find.add_argument("-ext",required=True)
preview = sub_parser.add_parser("preview")
preview.add_argument("-fp","--folder_path",required=True)
args = parser.parse_args()
if args.command == "organize":
    obj = FileOrganiser(args.folder_path)# question about args.fp why? 
    obj.organiser()
elif args.command == "find":
    obj = FileOrganiser(args.folder_path)
    founded_files = obj.find_files(args.ext)
    if not  founded_files:
        print(f"not file found with {args.ext}:(\n make sure you wrote .{args.ext} ")
    else:
        print(f"the found files are : \n{founded_files}")
elif args.command =="undo":
    obj = MoveLogger()
    obj.undo()
elif args.command == "history":
    obj = MoveLogger()
    obj.get_history()
elif args.command == "preview":
    obj = FileOrganiser(args.folder_path)
    obj.prevew()






