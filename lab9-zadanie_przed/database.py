from file_io import load_data_from_csv, load_data_from_json, save_data_to_csv, save_data_to_json


class FilePathNotFoundError(FileNotFoundError):
    pass


class FilePathIsDirectoryError(IsADirectoryError):
    pass


class FilePathPermissionError(PermissionError):
    pass


class Database():
    """
    Database class. Contains attributes:

    :param files: files located in database
    :type files: list[File]
    """

    def __init__(self) -> None:
        self.__files = []

    def load_data(self, path):
        ext = path.split(".")[-1]
        try:
            with open(path, "r") as filehandle:
                if ext == "csv":
                    self.__files = load_data_from_csv(filehandle)
                else:
                    self.__files = load_data_from_json(filehandle)

        except FileNotFoundError:
            raise FilePathNotFoundError("File not found")

        except IsADirectoryError:
            raise FilePathIsDirectoryError("Passed path is a directory")

        except PermissionError:
            raise FilePathPermissionError("No permission to open the file")

    def save_data(self, path):
        ext = path.split(".")[-1]
        try:
            with open(path, "w") as filehandle:
                if ext == "csv":
                    save_data_to_csv(filehandle, self.__files)
                else:
                    save_data_to_json(filehandle, self.__files)

        except FileNotFoundError:
            raise FilePathNotFoundError("File not found")

        except IsADirectoryError:
            raise FilePathIsDirectoryError("Passed path is a directory")

        except PermissionError:
            raise FilePathPermissionError("No permission to open the file")
