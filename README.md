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
git clone https://github.com/your-username/downloads-organizer.git
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

You can customize which extensions go into which folders by editing the extension lists inside the script.

## 🛠 Configuration

Inside the script:

```python
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
# etc.
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
