# File Organizer
A Python CLI tool that organizes your files by extension.
## Usage
```
python main.py organize -fp <path>
python main.py find -fp <path> -ext <extisions>
python main.py preview -fp <path>
python main.py undo
python main.py history
```
## Commands
- **organize** - moves files into subfolders named by extension
- **find** - returns all files with a given extension
- **preview** - show the changes before they happend
- **undo** -  upgraded from undoing only the last move to undoing all moves from the last organize session at once
- **history** - shows all logged moves
## Project Structure
```
file_organizer/
├── main.py
├── organizer.py
├── logger.py
└── README.md
```
