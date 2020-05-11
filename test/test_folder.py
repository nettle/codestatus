import imp
import os
import sys
import unittest


# Disable *.pyc files
sys.dont_write_bytecode = True


class TestFolder(unittest.TestCase):
    """Unittest class for Folder"""
    @classmethod
    def setUpClass(cls):
        """Load module"""
        cls.module_name = "folder"
        cls.module_path = "codestatus/folder.py"
        cls.module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, cls.module_path))
        cls.module = imp.load_source(cls.module_name, cls.module_path)
        os.chdir(os.path.abspath(os.path.dirname(__file__)))


    def test_folder(self):
        def print_folder(f, name=".", depth=0):
            print("%s%s = %s" % (depth * " ", name, f[name][0]))
            if f[name][1]:
                for item in f[name][1]:
                    print_folder(f[name][1], item, depth + 1)

        folder = self.module.Folder()
        self.assertEqual(folder.folder, {".": [None, None]})

        folder.add("a")
        self.assertEqual(folder.folder, {".": [None, {"a": [None, None]}]})

        folder.add("b/c/d", 111)
        self.assertEqual(
            folder.folder,
            {".": [111, {
                "a": [None, None],
                "b": [111, {"c": [111, {"d": [111, None]}]}]}]})

        folder.add("b/c/d", 222)
        self.assertEqual(
            folder.folder,
            {".": [333, {
                "a": [None, None],
                "b": [333, {"c": [333, {"d": [333, None]}]}]}]})

        folder.add("./b/c/d", 55)
        self.assertEqual(
            folder.folder,
            {".": [388, {
                "a": [None, None],
                "b": [388, {"c": [388, {"d": [388, None]}]}]}]})

        folder.add("e", 88)
        self.assertEqual(
            folder.folder,
            {".": [476, {
                "a": [None, None],
                "b": [388, {"c": [388, {"d": [388, None]}]}],
                "e": [88, None],
                }]
            })

        folder.add("f", 99)
        self.assertEqual(
            folder.folder,
            {".": [575, {
                "a": [None, None],
                "b": [388, {"c": [388, {"d": [388, None]}]}],
                "e": [88, None],
                "f": [99, None],
                }]
            })
        # print_folder(folder.folder)
