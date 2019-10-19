import shutil
import os


def main():
    # Cycle through files and ask user for directory name of file type
    # Do not ask twice
    # Do not create file twice if user wants to store 2 types in same one
    os.chdir('FilesToSort')
    directory_dictionary = {}
    for filename in os.listdir('.'):
        filename_extension = filename.split(".")[1]
        if filename_extension not in directory_dictionary:
            directory_name = input("What category would you like to sort {} files into? ".format(filename_extension))
            directory_dictionary[filename_extension] = directory_name
            try:
                os.mkdir(directory_name)
            except FileExistsError:
                pass
    for filename in os.listdir('.'):
        if "." in filename:
            filename_extension = filename.split(".")[1]
            shutil.move(filename, directory_dictionary[filename_extension] + "/" + filename)


main()
