import test_base


class TestFolder(test_base.TestBase):
    """Unittest class for Folder"""
    module_name = "folder"

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
