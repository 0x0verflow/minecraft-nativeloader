import json
import requests
from sys import argv
import zipfile
import os
import shutil

if len(argv) != 2 and len(argv) != 3:
    print("Usage: *.py <version.json>")
    print("       *.py <version.json> <output_folder>")
    print("")
    exit()

json_file = None
output_folder = "natives/"

if len(argv) > 1:
    json_file = argv[1]

if len(argv) > 2:
    output_folder = argv[2]

print(f"Trying to download natives from { json_file } to { output_folder }...")

json = json.load(open(json_file, "r"))

def extract(file):
    with zipfile.ZipFile(file, "r") as zip:
        zip.extractall(output_folder)

    try:
        shutil.rmtree(output_folder + "/META-INF")
    except:
        pass
    pass

try:
    os.mkdir(output_folder)
except:
    pass

try:
    os.mkdir(output_folder + "/temp")
except:
    pass

if not "libraries" in json:
    print("No libraries-field in JSON. Could it be corrupted?")
    exit()

for u in json["libraries"]:
    if "natives" in u:
        # Windows
        if "natives-windows" in u["downloads"]["classifiers"]:
            print(f"Downloading and extracting '{ u['name'] }' for Windows...")
            resp = requests.get(u["downloads"]["classifiers"]["natives-windows"]["url"])
            resp.raise_for_status()
            f = open(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-windows"]["url"]).split("/")[-1], "wb")
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
            f.close()

            extract(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-windows"]["url"]).split("/")[-1])
        else:
            print(f"No Windows native for { u['name'] } found! Skipping!")

        # MacOS
        if "natives-osx" in u["downloads"]["classifiers"]:
            print(f"Downloading and extracting '{ u['name'] }' for Osx...")
            resp = requests.get(u["downloads"]["classifiers"]["natives-osx"]["url"])
            resp.raise_for_status()
            f = open(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-osx"]["url"]).split("/")[-1], "wb")
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
            f.close()

            extract(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-osx"]["url"]).split("/")[-1])
        else:
            print(f"No Osx native for { u['name'] } found! Skipping!")

        # Linux
        if "natives-linux" in u["downloads"]["classifiers"]:
            print(f"Downloading and extracting '{ u['name'] }' for Linux...")
            resp = requests.get(u["downloads"]["classifiers"]["natives-linux"]["url"])
            resp.raise_for_status()
            f = open(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-linux"]["url"]).split("/")[-1], "wb")
            for chunk in resp.iter_content(chunk_size=8192):
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            f.close()

            extract(str(output_folder) + "/temp/" + str(u["downloads"]["classifiers"]["natives-linux"]["url"]).split("/")[-1])
        else:
            print(f"No Linux native for { u['name'] } found! Skipping!")

shutil.rmtree(output_folder + "/temp")
print("Done!")
exit()
