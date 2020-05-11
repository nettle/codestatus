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


def test():
    folder = Folder()
    print(folder.folder)
    folder.add("aaa")
    print(folder.folder)
    folder.add("bbb/ccc/ddd", 111)
    print(folder.folder)
    folder.add("bbb/ccc/ddd", 222)
    print(folder.folder)
    folder.add("./bbb/ccc/ddd", 55)
    print(folder.folder)
    folder.add("eee", 88)
    folder.add("fff", 99)

    def print_folder(f, name=".", depth=0):
        print("%s%s = %s" % (depth * " ", name, f[name][0]))
        if f[name][1]:
            for item in f[name][1]:
                print_folder(f[name][1], item, depth + 1)

    print_folder(folder.folder)
