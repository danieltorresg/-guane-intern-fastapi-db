import os

from requests import post


def upload_file():
    url = "https://gttb.guane.dev/api/files"
    path = r"./app/utils"
    files = {
        "file": ("file.txt", open(os.path.join(path, "file.txt")), "rb"),
    }
    response = post(url, files=files)
    return response.json()
