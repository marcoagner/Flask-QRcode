import sys
from pathlib import Path


SNAPSHOT_DIR = Path(__file__).with_name("snapshot_data")


def get_expected_b64(name, original):
    if name.startswith("svg_"):
        if sys.version_info >= (3, 8):
            return original
        directory = "python_3_7"
    elif name == "remote_icon":
        if sys.version_info < (3, 9):
            directory = "python_3_7_8"
        elif sys.version_info < (3, 10):
            directory = "python_3_9"
        else:
            directory = "python_3_10_plus"
    elif sys.version_info >= (3, 10):
        directory = "python_3_10_plus"
    elif sys.version_info >= (3, 9):
        directory = "python_3_9"
    else:
        return original

    return (SNAPSHOT_DIR / directory / (name + ".b64")).read_text(encoding="ascii")