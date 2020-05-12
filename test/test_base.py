import imp
import os
import unittest


class TestBase(unittest.TestCase):
    """Abstract unittest TestBase class"""
    module_dir = "codestatus"

    @classmethod
    def setUpClass(cls):
        """Load module"""
        # NOTE: module_name must be defined in superclass
        cls.module_path = os.path.join(cls.module_dir, cls.module_name + ".py")
        cls.module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, cls.module_path))
        cls.module = imp.load_source(cls.module_name, cls.module_path)
