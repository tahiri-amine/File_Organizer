# File Organizer
A Python CLI tool that organizes your files by extension.
## Usage
python main.py organize ./my_folder
python main.py find ./my_folder .txt
python main.py undo
python main.py history
## Commands
- **organize** - moves files into subfolders named by extension
- **find** - returns all files with a given extension
- **undo** - reverses the last move
- **history** - shows all logged moves
## Project Structure
file_organizer/
├── main.py
├── organizer.py
├── logger.py
└── README.md