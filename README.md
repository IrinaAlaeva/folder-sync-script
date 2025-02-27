# Folder Synchronization Script

This Python script synchronizes a source folder with a replica folder by copying, updating, and deleting files accordingly.

## Features
- Recursively syncs all files and folders.
- Detects changes using MD5 checksums.
- Logs operations (file copy, delete).
- Runs on a scheduled interval.

Run the script with:
python sync.py <source_folder> <replica_folder> --interval <seconds> --log <logfile>