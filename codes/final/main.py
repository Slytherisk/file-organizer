from pathlib import Path
import shutil
import os
import re

list_file = os.listdir()
for file in list_file:
    if not(Path.is_dir(file)):
        format = re.search(r"\.\w+$", file).group()
        match format:
            case ".jpg" | ".png" | ".jpeg":
                try:
                    Path.mkdir("Picture")
                    shutil.move(file, "Picture")
                except FileExistsError:
                    shutil.move(file, "Picture")

            case ".wav" | ".mp3":
                try:
                    Path.mkdir("Music")
                    shutil.move(file, "Music")
                except FileExistsError:
                    shutil.move(file, "Music")

            case ".zip" | ".rar":
                try:
                    Path.mkdir("Compressed")
                    shutil.move(file, "Compressed")
                except FileExistsError:
                    shutil.move(file, "Compressed")

            case ".epub":
                try:
                    Path.mkdir("Book")
                    shutil.move(file, "Book")
                except FileExistsError:
                    shutil.move(file, "Book")

            case ".exe":
                try:
                    Path.mkdir("Program")
                    shutil.move(file, "Program")
                except FileExistsError:
                    shutil.move(file, "Program")

            case ".mp4":
                try:
                    Path.mkdir("Video")
                    shutil.move(file, "Video")
                except FileExistsError:
                    shutil.move(file, "Video")

            case ".pdf" | ".PDF" | ".txt":
                try:
                    Path.mkdir("Document")
                    shutil.move(file, "Document")
                except:
                    shutil.move(file, "Document")

            case _:
                if file != "main.py":
                    try:
                        Path.mkdir("Unknown")
                        shutil.move(file, "Unknown")
                    except:
                        shutil.move(file, "Unknown")
