from csv import reader
from subprocess import run
from os import chdir, getcwd


def get_list_of_folders() -> list:
    """
    Return list of folder
    :return:
    """
    return run(["find . -mindepth 1 -maxdepth 1 -type d | cut -d / -f 2"],
               text=True, shell=True, capture_output=True).stdout.split()


def get_list_of_files() -> list:
    """
    Returns list of csv files in the current dir
    :return:
    """
    return run(["ls | grep .csv"], text=True, shell=True, capture_output=True).stdout.split()


def main():
    root_dir = getcwd()

    chdir("Items")

    for folder in get_list_of_folders():
        chdir(folder)

        for file in get_list_of_files():
            # Sort file content (Maybe by functions)
            pass

        chdir("..")


if __name__ == '__main__':
    main()
