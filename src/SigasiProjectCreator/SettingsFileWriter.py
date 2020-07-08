import os


def write(destination, name, content):
    library_mapping_file = os.path.abspath(os.path.join(destination, name))
    with open(library_mapping_file, "wb") as f:
        f.write(content.encode())
