"""
Cppcheck is a static analysis tool for C/C++ code

Requires: cppcheck version 1.70 (1.90? 2.0?)

Install in Ubuntu:

    sudo apt-get install cppcheck

Download:
- http://cppcheck.sourceforge.net/
- https://github.com/danmar/cppcheck
"""

import logging

import utils


class CppCheck:
    """FIXME"""
    def __init__(self):
        """FIXME"""
        logging.debug("CppCheck: init")

    def run(self):
        """FIXME"""
        logging.debug("CppCheck: running...")
        # template = """--template='{\n\t"file": "{file}",\n\t"line": "{line}",\n\t"column": "{column}",\n\t"callstack": "{callstack}",\n\t"text": "{inconclusive:text}",\n\t"severity": "{severity}",\n\t"message": "{message}",\n\t"id": "{id}",\n\t"cwe": "{cwe}",\n\t"code": "{code}"\n},'"""
        # logging.debug("Running: cppcheck...")
        # utils.execute("cppcheck -q " + template + " " + self.options.path)
