import os
import sys


def ex1():
    def print_file_contents(file_name):
        try:
            with open(file_name) as f:
                for line in f:
                    print(line.strip())
        except OSError as e:
            raise OSError(f"Unable to open file {file_name}") from e

    def read_files(dir_path, file_ext):
        if not file_ext.isalpha():
            raise ValueError(f"File extension {file_extension} is not valid")
        if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
            raise FileNotFoundError("Invalid directory path or directory does not exist")

        files = os.listdir(dir_path)

        for file_name in files:
            if file_name.endswith(f".{file_ext}"):
                full_file_name = os.path.join(dir_path, file_name)
                print_file_contents(full_file_name)

    if len(sys.argv) != 3:
        raise ValueError("Script takes 2 parameters")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        read_files(directory_path, file_extension)


def ex2():
    def rename_files(dir_path):
        if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
            raise FileNotFoundError("Directory name not valid or directory does not exist")

        files = os.listdir(dir_path)
        files.sort()

        for (index, file_name) in enumerate(files, start=1):
            full_file_name = os.path.join(dir_path, file_name)
            new_file_name = os.path.join(dir_path, f"file{index}{os.path.splitext(full_file_name)[1]}")
            try:
                os.rename(full_file_name, new_file_name)
            except Exception as e:
                raise Exception(f"File {full_file_name} could not be renamed as {new_file_name}") from e

    if len(sys.argv) != 2:
        raise Exception("Script takes 1 parameter")
    directory_name = sys.argv[1]
    rename_files(directory_name)


def ex3():
    def directory_size(dir_path):
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError("Directory name not valid or directory does not exist")
        files = os.listdir(dir_path)
        total_size = 0
        for file in files:
            full_file_name = os.path.join(dir_path, file)
            if os.path.isdir(full_file_name):
                total_size += directory_size(full_file_name)
            else:
                try:
                    size = os.path.getsize(full_file_name)
                    total_size += size
                except OSError as e:
                    raise OSError(f"Error accessing {full_file_name}") from e
        return total_size

    if len(sys.argv) != 2:
        raise Exception("Script takes 1 argument")
    directory_path = sys.argv[1]
    print(directory_size(directory_path))

