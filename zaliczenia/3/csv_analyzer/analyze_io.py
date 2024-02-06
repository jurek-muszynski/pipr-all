from os import listdir
from file import File
import csv
import json


class MalformedCsvDataError(Exception):
    def __init__(self, args) -> None:
        super().__init__(args)


def find_csv_files(dir):
    filenames = listdir(dir)
    return [filename for filename in filenames if filename[-4:] == ".csv"]


def get_count_values(fieldnames_dict):
    fieldnames_values_count = {}
    for key, values in fieldnames_dict.items():
        fieldnames_values_count[key] = {
            value: values.count(value) for value in values
        }
    return (fieldnames_values_count)


def get_unique_values(fieldnames_unique_dict):
    return {
        fieldname: len(fieldnames_unique_dict[fieldname])
        for fieldname in fieldnames_unique_dict
    }


def get_files_data(file_names, directory):
    files = []
    for file_name in file_names:
        try:
            path = f"{directory}/{file_name}"
            with open(path) as filehandle:
                files.append(load_from_file(
                    path, filehandle))

        except PermissionError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    return files


def load_from_file(path, filehandle):
    try:
        reader = csv.DictReader(filehandle)
        fieldnames = reader.fieldnames
        if None in fieldnames or "" in fieldnames:
            raise MalformedCsvDataError(
                f"{path}: Column names cannot be empty")
        fieldnames_unique_dict = {fieldname: [] for fieldname in fieldnames}
        fieldnames_dict = {fieldname: [] for fieldname in fieldnames}
        rows = 0
        for row in reader:
            rows += 1
            for field in fieldnames:
                value = row[field]
                if value not in fieldnames_unique_dict[field]:
                    fieldnames_unique_dict[field].append(value)
                fieldnames_dict[field].append(value)
        fieldnames_values_count = get_count_values(fieldnames_dict)
        fieldnames_values_unique = get_unique_values(fieldnames_unique_dict)
        return File(path, fieldnames, rows,
                    fieldnames_values_unique, fieldnames_values_count)
    except csv.Error as e:
        raise MalformedCsvDataError(str(e))


def save_to_file(path, data):
    with open(path, "w") as filehandle:
        json.dump(data, filehandle, indent=6)
