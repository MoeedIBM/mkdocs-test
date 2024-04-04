import os

"""
Test Python Script - Used for testing sphinx auto doc generation
...
"""

__version__ = "0.1.0"

def list_directories(path):
    """
    Gets a list of directories.

    Takes in a path argument and returns a list of strings with the names of the directories.

    Parameters:
    path (str): path string
    ...

    Returns:
    list[str]: List of strings representing directory names.
    """
    directories = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
    return directories



def main():
    """
    Main function to list directories on the desktop.
    ...
    """
    desktop_path = os.path.expanduser("~/Desktop")
    directories = list_directories(desktop_path)
    if directories:
        print("Directories on Desktop:")
        for directory in directories:
            print(directory)
            print("--------")
    else:
        print("No directories found on Desktop.")

if __name__ == "__main__":
    main()
