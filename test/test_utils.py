import imp
import os
import sys
import unittest


# Disable *.pyc files
sys.dont_write_bytecode = True


class TestUtils(unittest.TestCase):
    """Unittest class for utils"""
    @classmethod
    def setUpClass(cls):
        """Load module"""
        cls.module_name = "utils"
        cls.module_path = "codestatus/utils.py"
        cls.module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, cls.module_path))
        cls.module = imp.load_source(cls.module_name, cls.module_path)
        os.chdir(os.path.abspath(os.path.dirname(__file__)))


    def test_execute(self):
        """Test execute()"""
        self.assertEqual(self.module.execute("true"), "")
        self.assertEqual(self.module.execute("echo 1"), "1\n")

    def test_available(self):
        """Test available()"""
        self.assertTrue(self.module.available("true"))
        self.assertFalse(self.module.available("something-wrong"))
