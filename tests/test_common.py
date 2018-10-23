import os
import pytest

from .conftest import DatalightException, get_files_path, zipdata

# Path where the tests are
_dir = os.path.dirname(os.path.realpath(__file__))

dir = 'common'
fname1 = 'test_common1.dat'
fname2 = 'test_common2.dat'
fpath1 = os.path.join(dir, fname1)
fpath2 = os.path.join(dir, fname2)

def test_get_files_path_file():
    assert [fpath1] == get_files_path(fpath1)


def test_get_files_path_directory():
    assert [fpath1, fpath2] == get_files_path(dir)


def test_get_files_path_exception():
    with pytest.raises(DatalightException):
        get_files_path('doesnotexist')


def test_zipdata_nofile_or_file_does_not_exist():
    with pytest.raises(DatalightException):
        zipdata('')


def test_zipdata_with_existing_file():
    zipdata(fpath1)
    assert os.path.isfile('data.zip')


def test_zipdata_wrong_input():
    with pytest.raises(DatalightException):
        zipdata(1233)


def test_zipdata_directory_as_input():
    zipdata(dir)
    assert os.path.isfile('data.zip')
    os.remove('data.zip')


def test_zipdata_save_zip_another_name():
    zipdata(dir, 'toto.zip')
    assert os.path.isfile('toto.zip')
    os.remove('toto.zip')
