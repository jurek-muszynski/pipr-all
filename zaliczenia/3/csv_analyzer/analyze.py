import sys
import argparse
from analyze_io import MalformedCsvDataError, find_csv_files, get_files_data, save_to_file
import os


class InvalidFilesDataError(MalformedCsvDataError):
    pass


def get_columns(file):
    return f"columns: {file.fieldnames}\n"


def get_rows(file):
    return f"rows: {file.rows}\n"


def get_unique(file):
    return f"unique: {file.unique_values}\n"


def get_count(file):
    return f"counted values: {file.count_values}\n"


def main(arguments):
    parser = argparse.ArgumentParser()

    parser.add_argument("directory")
    parser.add_argument("--columns", action="store_true")
    parser.add_argument("--rows", action="store_true")
    parser.add_argument("--unique", action="store_true")
    parser.add_argument("--count", action="store_true")
    parser.add_argument("--out", nargs="?")
    parser.add_argument("-f", action="store_true")
    args = parser.parse_args(arguments[1:])

    file_names = []
    directory = args.directory
    if directory:
        try:
            file_names = find_csv_files(args.directory)
            if file_names:
                try:
                    files = get_files_data(file_names, directory)
                    files_list = {}
                    for file in files:
                        file_str = f"{file.path}\n"
                        data = {}
                        if args.columns:
                            file_str += get_columns(file)
                            data["columns"] = file.fieldnames
                        if args.rows:
                            file_str += get_rows(file)
                            data["rows"] = file.rows
                        if args.unique:
                            file_str += get_unique(file)
                            data["unique"] = file.unique_values
                        if args.count:
                            file_str += get_count(file)
                            data["count"] = file.count_values
                        print(file_str)
                        files_list[file.path] = data
                    if args.out:
                        if args.f:
                            save_to_file(args.out, files_list)
                        else:
                            if os.path.exists(args.out):
                                overwrite = input(
                                    f"There already exists a file called {args.out}, would you like to overwrite it ?: ")
                                if overwrite in ["yes", "Y",
                                                 "y", "Yes", "YES"]:
                                    save_to_file(args.out, files_list)
                            else:
                                save_to_file(args.out, files_list)

                except MalformedCsvDataError as e:
                    raise InvalidFilesDataError() from e
                except Exception as e:
                    print(str(e))
            else:
                print("no .csv files were found in the following directory")
        except FileNotFoundError as e:
            print(str(e))


if __name__ == "__main__":
    main(sys.argv)
