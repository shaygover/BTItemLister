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

        # Line lists
        new_items = list()

        for file in get_list_of_files():
            # Open the file
            with open(file, newline='', encoding='utf_8') as item_collections:
                items_reader = reader(item_collections, delimiter=',', quotechar='|')

                # lose the first line
                items_reader.__next__()

                # Iterate the lines
                for line in items_reader:
                    if line[1] != "Reference":
                        new_items.append(",".join(line))

        # Remove duplicate cells
        unique_items = list()
        [unique_items.append(item) for item in new_items if item not in unique_items]

        # Print to list.txt file
        output_file = open("00" + folder + ".txt", "w")

        for item in unique_items:
            output_file.write(item + "\n")

        output_file.close()
        chdir("..")

    chdir("..")

    print("Original Root: ", root_dir, "\n")
    print("Current Root: ", getcwd(), "\n")

    print("Done")


if __name__ == '__main__':
    main()
