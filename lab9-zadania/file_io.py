from zipfile import ZipFile
from pathlib import Path


def extract_files(path):
    try:
        with ZipFile(path) as myzip:
            myzip.extractall()
    except Exception as e:
        return str(e)
    mydir = Path(path.split(".")[0])
    text_files = list(mydir.glob('**/*.txt'))
    text_files = sorted(text_files, key=lambda file: file.name)
    return text_files


def load_text(files):
    loaded_text = ""
    for file in files:
        try:
            with open(file) as filehandle:
                loaded_text += f"{filehandle.readline()} "
        except Exception as e:
            return str(e)
    return loaded_text


def main():
    files = extract_files("documents.zip")
    text_from_files = load_text(files)
    print(text_from_files)


if __name__ == "__main__":
    main()
