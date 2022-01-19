# tsv_handler
Script for downloading and sorting tsv spreadsheets exported from Oracle R12

# --- What it does ---
This script automatically opens all files exported from Oracle whose name is "fnd_gfm_XXXXXXX.tsv", right after download. 


# --- How it works ---
The script recognizes files named "fnd... .tsv" that appear in the "Download" folder, and then moves them to "tsv" subdirectory, where the newest item* is opened. 
*newest by its name- all files are renamed (current date with seconds added) before moving them to /tsv directory, so most recently downloaded file will always be first on the list of all downloaded .tsv


# --- Requirements ---
[1-3: you do it once | 4: if the script doesn't crash you do it once a day- before you start downloading any files | 5: always do it before exporting anything from Oracle]

1) Create "Download" folder on your desktop with a "tsv" subfolder in it.
2) Set up your browser so that all files are downloaded into the "Download" folder.
3) Unpack the tsv_handler zipped file, place it anywhere you want on your drive, you can create a shortcut to the .exe file and also store it anywhere you want.
4) Activate the script by double-clicking the .exe file called tsv_handler. The app will keep working in the background until you end the process through task manager (find 'tsv_handler' on the list), or until the script errors out - then a message will prompt you to restart the app.
5) Before downloading any .tsv files you probably need to have an excel instance already running, otherwise the script will still try to open the file, but what you'll see is a blank gray screen (you can just close it). It's some kind of incompatibility of .tsv format with excel, but the script will keep working in the background if that happens.



# --- Notes ---
* It makes no difference what browser you use for downloads. <br/>
* If you manually copy a file named "fnd_gfm_XXXXXX.tsv" into "Download" - it will be renamed, then moved to "tsv" folder, and then opened. Same as if you downloaded it. <br/>
* The script doesn't produce any additional/temporary files on your drive. It terminates on system closure or if you kill it via task manager.