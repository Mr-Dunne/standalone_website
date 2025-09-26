import os
import shutil

def copy_directory_contents(source, destination):
    """
    Recursively copies all contents from a source directory to a destination directory.
    First, it cleans the destination directory.
    """
    # 1. Clean the destination directory
    if os.path.exists(destination):
        print(f"Removing existing directory contents at: {destination}")
        shutil.rmtree(destination)

    # 2. Create the new destination directory
    print(f"Creating new destination directory at: {destination}")
    os.mkdir(destination)

    # 3. Call the recursive helper function
    _copy_recursive(source, destination)
    print("All files copied successfully.")


def _copy_recursive(source_path, destination_path):
    """
    A helper function to recursively copy files and directories.
    """
    # Get a list of all items in the current source directory
    for item in os.listdir(source_path):
        current_source = os.path.join(source_path, item)
        current_destination = os.path.join(destination_path, item)

        # Check if the item is a file (the base case for recursion)
        if os.path.isfile(current_source):
            print(f"  Copying file: {current_source} -> {current_destination}")
            shutil.copy(current_source, current_destination)

        # If the item is a directory, recurse
        elif os.path.isdir(current_source):
            print(f"  Entering directory: {current_source}")
            os.mkdir(current_destination)
            _copy_recursive(current_source, current_destination)