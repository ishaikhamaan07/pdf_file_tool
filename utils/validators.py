import os


def validate_path(path):
    """
    Check whether the given path exists and is a directory.
    """

    if not path:
        return False

    if os.path.exists(path) and os.path.isdir(path):
        return True

    return False