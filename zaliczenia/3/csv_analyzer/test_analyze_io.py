from analyze_io import (get_count_values, get_unique_values,
                        get_files_data, load_from_file)
from io import StringIO
from file import File


def test_analyze_load_from_file():
    data = "id,name,pesel\nid1,name1,pesel1\nid2,name1,pesel1"
    filehandle = StringIO(data)
    file = load_from_file("file.csv", filehandle)
    assert file.path == "file.csv"
    assert file.fieldnames == ["id", "name", "pesel"]
    assert file.unique_values == {"id": 2, "name": 1, "pesel": 1}
    assert file.count_values == {"id": {"id1": 1, "id2": 1}, "name": {
        "name1": 2}, "pesel": {"pesel1": 2}}
