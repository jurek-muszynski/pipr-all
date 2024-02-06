from file import File


def test_create_file_std():
    file = File("file.csv", ["field1", "field2"],
                2, {"field1": 2, "field2": 1},
                {"field1": {"value1": 1}})
    assert file.path == "file.csv"
    assert file.fieldnames == ["field1", "field2"]
    assert file.unique_values == {"field1": 2, "field2": 1}
    assert file.count_values == {"field1": {"value1": 1}}
