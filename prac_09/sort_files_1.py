import shutil
import os


def main():
    os.chdir('FilesToSort')
    # print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for filename in os.listdir('.'):
        directory_name = filename.split(".")[1]
        print(directory_name)
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            pass
        shutil.move(filename, directory_name + "/" + filename)


main()
