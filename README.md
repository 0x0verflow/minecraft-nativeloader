# minecraft-nativeloader
Python script to download LWJGL/... natives for Minecraft which can be used to run Minecraft in an unofficial launcher for "modding"

## Usage
Use the following command to download some chonky libraries to your hard-drive without using the Minecraft Launcher:
```bash
python3 nativeloader.py <version.json> [<output_folder> - optional]
python3 nativeloader.py 1.9.json 
python3 nativeloader.py 1.9.json /home/haxx0r/mc_natives
```

You can find the version.json (e.g. `1.12.json`) in `.minecraft/versions/<version>/<version>.json` or download it directly from the Mojang servers.
