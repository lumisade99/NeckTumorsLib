from os import listdir

from RadImaLib.utils import add_dicom_extension


def test_add_dicom_extension():
    directory = 'tests/test_files'
    add_dicom_extension(directory)
    files = [f for f in listdir(directory)]
    print(str(files))
    error_counter = 0
    for file in files:
        if file[-1] != 'm':
            error_counter += 1
    assert error_counter == 0

