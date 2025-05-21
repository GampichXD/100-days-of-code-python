# Professional Portfolio Project - Python Automation
# Custom Automation
# Author : Abraham
import os
import shutil

# Define file type mapping
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.jpeg', '.gif'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Software': ['.exe', '.msi', '.dmg'],
}

DOWNLOAD_DIR = os.path.expanduser('~/Downloads')

def organize_downloads():
    for filename in os.listdir(DOWNLOAD_DIR):
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    dest_dir = os.path.join(DOWNLOAD_DIR, folder)
                    os.makedirs(dest_dir, exist_ok=True)
                    try:
                        shutil.move(filepath, os.path.join(dest_dir, filename))
                    except PermissionError:
                        print(f"⚠️ File in use, skipped: {filename}")
                    break


if __name__ == "__main__":
    organize_downloads()
    print("Download folder organized.")
