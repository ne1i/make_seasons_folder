import os
import re
import shutil

cwd = os.curdir

video_extensions = (
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
    ".mkv",
    ".mpeg",
    ".mpg",
    ".3gp",
    ".m4v",
    ".vob",
    ".ts",
    ".m2ts",
)


def is_correct_file(file: os.DirEntry):
    contains_serie_pattern = re.search(r"[sS]\d{1,2}", str(file.name)) is not None
    return (
        file.is_file()
        and str(file.name).endswith(video_extensions)
        and contains_serie_pattern
    )


def get_series_id(file: os.DirEntry):
    match = re.search(r"[sS](?:\d{1,2})", file.name)
    if match:
        return match.group()


with os.scandir(cwd) as entries:
    for entry in entries:
        if is_correct_file(entry):
            folder_name = get_series_id(entry)
            folder_path = os.path.join(cwd, folder_name)
            if folder_name not in os.listdir(cwd):
                os.mkdir(folder_name)
                shutil.move(entry.path, folder_path)
            else:
                shutil.move(entry.path, folder_path)
                print("Moved", entry.name, "to", folder_name)
