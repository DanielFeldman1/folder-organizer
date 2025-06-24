# 🗂️ Downloads Folder Organizer

A simple and reversible Python script to organize your Downloads folder by file type: images, documents, videos, and more.

## ⚙️ Features

- ✅ Automatically organizes files into folders by type  
- ✅ Reversible: undo and restore original file locations  
- ✅ Lightweight and easy to customize  
- ✅ No external libraries needed  

## 🚀 Getting Started

1. **Clone the repository**  
```bash
git clone https://github.com/DanielFeldman1/folder-organizer.git
cd downloads-organizer
```

2. **Run the script**  
```bash
python FolderOrganizer.py
```

3. **Undo changes (optional)**  
```bash
python FolderOrganizerReverser.py
```
![Untitled](https://github.com/user-attachments/assets/66b1652a-92df-4f0b-baca-7f58fda7b5c7)



## 🧠 How It Works

The script scans your Downloads folder and moves files into subfolders based on their extensions:

```
Downloads/
├── Images/
├── Videos/
├── Documents/
├── Audio/
└── Others/
```
Before:

![folder-organizer1](https://github.com/user-attachments/assets/23c5ccad-2bac-456a-a731-6f50143fbad2)

After:

![folder-organizer2](https://github.com/user-attachments/assets/118f6a18-54ac-421c-9c49-985167361b82)

Saved paths in json:

![folder-organizer3](https://github.com/user-attachments/assets/d81e4374-6648-4f6e-ab96-1ee013b98921)

You can customize which extensions go into which folders by editing the extension lists inside the script.

## 🛠 Configuration

Inside the script:

```python
# Choose file extensions
image_extensions = {".jpg",".HEIC",".JPEG",".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heic", ".raw", ".cr2", ".nef", ".orf", ".sr2"}
video_extensions = {".mp4",".MP4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"}
audio_extensions = {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"}
document_extensions = {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".tex", ".md",".pages"}
spreadsheet_extensions = {".xls", ".xlsx", ".csv", ".ods", ".tsv", ".xlsm"}
presentation_extensions = {".ppt", ".pptx", ".odp", ".key"}
archive_extensions = {".zip",".ZIP", ".rar", ".7z", ".tar", ".gz", ".bz2",".tgz"}
code_extensions = {".ipynb",".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".ts", ".json", ".xml", ".sh"}
exe_extensions = {".exe",".msi",".ica"}
diagram_extensions = {".drawio",".vpp",".bak_000f",".tdl"}
book_extensions = {".epub"}

# Choose where they go
if file_extension in image_extensions:
    return Path(os.path.join(user_home,"Pictures"))
elif file_extension in video_extensions:
    return Path(os.path.join(user_home,"Videos"))
elif file_extension in audio_extensions:
    return Path(os.path.join(user_home,"Music"))
elif file_extension in document_extensions:
    return Path(os.path.join(user_home,"Documents/Documents"))
elif file_extension in spreadsheet_extensions:
    return Path(os.path.join(user_home,"Documents/Spreadsheets"))
elif file_extension in presentation_extensions:
    return Path(os.path.join(user_home,"Documents/Presentations"))
elif file_extension in archive_extensions:
    return Path(os.path.join(user_home,"Documents/Archives"))
elif file_extension in code_extensions:
    return Path(os.path.join(user_home,"Documents/Code Files"))
elif file_extension in exe_extensions:
    return Path(os.path.join(user_home,"Documents/Executables"))
elif file_extension in diagram_extensions:
    return Path(os.path.join(user_home,"Documents/Diagrams"))
elif file_extension in book_extensions:
    return Path(os.path.join(user_home,"Documents/Books"))
else:
    return Path(os.path.join(user_home,"Documents/Others"))
```

Modify these lists to match your preferences.

## 🐍 Requirements

- Python 3.x  
- No external dependencies

## 📄 License

MIT License — use it, fork it, customize it.

## 🙋‍♂️ Author

Made by Daniel Feldman 
If you find this helpful, feel free to ⭐ the repo or open an issue with feedback!
