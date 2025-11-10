# TWorkshopDL 

Simple steam workshop download utility for terraria. Useful for downloading content such as resourcepacks which is not possible to download via tmodloader. This tool is probably useless to you if you own terraria from Steam and can directly subscribe these workshop items, but is really useful for players who own terraria from other sources such as GOG. 

## Dependencies & other requirements

- Python >= 3.10 
- Steam (native installation, flatpak might work but there is no guarantees)
- [steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD)
- Program assumes that there is command called `steamcmd` available in PATH. 

## Installation

### Clone repository
>$ git clone https://github.com/syomasa/tworkshopdl

### Ensure correct permissions
>$ cd tworkshopdl

>$ chmod +x run_tworkshopdl.sh 

### (Optional) Create symbolic link to ~/.local/bin to make it available everywhere
>$ ln -s ~/path/to/script.sh ~/.local/bin/tworkshopdl

To test everything works run `tworkshopdl -h`

## Usage

### Download workshop item into default steamapps location
>$ ./run_tworkshopdl.sh  \<workshop-item-id\>

### Download workshop item into specific directory
>$ ./run_tworkshopdl.sh --download-dir path/to/your/dir \<workshop-item-id\>

### Create missing directories first and download workshop item into that directory
>$ ./run_tworkshopdl.sh -p --download-dir path/to/your/dir \<workshop-item-id\>


## Additional notes

Because program is basically just wrapper to steamcmd workshop_download_item functionality adapting this to different games is also possible as long as their workshop doesn't require login to work. You can do this easily by changing `TERRARIA_GAME_ID` parameter in `terraria_workshop_loader.py` file into id of the other game you want to use this for. You can view game ids quite easily using sites like [steamDB](https://https://steamdb.info/)



