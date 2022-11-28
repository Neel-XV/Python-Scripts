import os
import json
import requests
from io import BytesIO
from zipfile import ZipFile

with open("config.json", "r") as cfg:
    data = json.load(cfg)
    cfg.close()

url = "https://settings.gg/download/" + data["steamID3"]
r = requests.get(url, allow_redirects=True)


def main():
    dir = (
        "C:\\Program Files\\Steam\\userdata\\" + data["steamID3"] + "\\730\\local\\cfg"
    )
    if os.path.exists(dir):
        local_disk_directory = "C"
    else:
        local_disk_directory = "D"
        dir = local_disk_directory + dir[1:]
    print(f"Directory Identified As {local_disk_directory}")

    z = ZipFile(BytesIO(r.content))
    z.extractall(dir)
    print("Configuration Updated")
    z.close()


if __name__ == "__main__":
    main()
