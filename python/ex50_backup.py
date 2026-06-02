import shutil
import os

def backup_files(source_files, backup_folder):
    copied_files = set()

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    log_file = open("backup.log", "a")

    for file in source_files:
        try:
            if file in copied_files:
                log_file.write(f"SKIPPED (duplicate): {file}\n")
                continue

            if not os.path.exists(file):
                log_file.write(f"NOT FOUND: {file}\n")
                continue

            destination = os.path.join(backup_folder, os.path.basename(file))
            shutil.copy(file, destination)

            copied_files.add(file)
            log_file.write(f"COPIED: {file} -> {destination}\n")

        except PermissionError:
            log_file.write(f"PERMISSION ERROR: {file}\n")
        except Exception as e:
            log_file.write(f"ERROR: {file} -> {e}\n")

    log_file.close()
    print("Backup completed. Check backup.log")

files = input("Enter file names separated by space: ").split()
backup_folder = "backup"

backup_files(files, backup_folder)