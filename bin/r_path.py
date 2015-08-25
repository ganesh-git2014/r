import tempfile
import os

tempdir = tempfile.gettempdir()
tempdir_segment = 'r_v7'
_existing_paths = set()


def delete_path_root():
    import shutil
    p = os.path.join(tempdir, tempdir_segment)
    if os.path.exists(p):
        shutil.rmtree(p)
    _existing_paths.clear()


def get_file(name):
    p = os.path.join(tempdir, tempdir_segment)
    if p not in _existing_paths:
        if not os.path.exists(p):
            os.makedirs(p)
        _existing_paths.add(p)
    return os.path.join(p, name)


def get_directory(*segments):
    p = os.path.join(tempdir, tempdir_segment)
    for name in segments:
        p = os.path.join(p, name)
        if p not in _existing_paths:
            if not os.path.exists(p):
                os.makedirs(p)
            _existing_paths.add(p)
    return p