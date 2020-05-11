"""
"""

class Folder(object):
    """Abstract Folder class"""
    def __init__(self):
        self.folder = {
            ".": [     # Folder/file name
                None,  # Data
                None,  # Children as dict
            ],
        }

    def add(self, name, data=None):
        folder = self.folder["."]
        if not folder[0]:
            folder[0] = data
        else:
            folder[0] += data
        for directory in name.split("/"):
            if directory == ".":
                continue
            else:
                folder = self.add_to(directory, data, folder)

    def add_to(self, name, data, folder):
        if not folder[1]:
            folder[1] = {}
        if name not in folder[1]:
            folder[1][name] = [data, None]
        else:
            folder[1][name][0] += data
        return folder[1][name]
