#!/usr/bin/env python

"""
CodeStatus script

This script collects code metrics
FIXME: description
"""

from __future__ import print_function
import argparse
# import datetime
# import glob
import logging
import os
# import re
import shlex
# import shutil
import subprocess

import utils


CODESTATUS_EXAMPLES = """
examples:

  # "Dry run" to see commands without execution:
  codestatus ?
"""
# FIXME: examples


class CodeStatus(object):
    """
    This class is a launcher
    FIXME: class description
    """
    def parse_args(self):
        """
        Parse command line arguments or show help.
        """
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                         description=__doc__,
                                         epilog=CODESTATUS_EXAMPLES)
        parser.add_argument("-v", "--verbosity",
                            default=0,
                            action="count",
                            help="Increase output verbosity (e.g., -v or -vv)")
        parser.add_argument("-n", "--dry-run",
                            default=False,
                            action="store_true",
                            help="Just print CodeStatus commands without running them")
        parser.add_argument("--log-format",
                            default="[codestatus] %(levelname)5s: %(message)s",
                            help=argparse.SUPPRESS)
        parser.add_argument("path",
                            nargs="?",
                            default="./",
                            help="Path to the source code folder")

        self.options = parser.parse_args()

        if self.options.verbosity >= 2:
            log_level = logging.DEBUG
        elif self.options.verbosity >= 1:
            log_level = logging.INFO
        else:
            log_level = logging.WARN
        logging.basicConfig(level=log_level, format=self.options.log_format)

        logging.debug("Options: %s", self.options)

        if not os.path.isdir(self.options.path):
            logging.error("The path specified does not exist")
            exit(1)

    def run(self):
        """
        Run CodeStatus
        """
        self.parse_args()
        logging.debug("Running: sw_metrics...")
        utils.execute("sw_metrics " + self.options.path)
        template = """--template='{\n\t"file": "{file}",\n\t"line": "{line}",\n\t"column": "{column}",\n\t"callstack": "{callstack}",\n\t"text": "{inconclusive:text}",\n\t"severity": "{severity}",\n\t"message": "{message}",\n\t"id": "{id}",\n\t"cwe": "{cwe}",\n\t"code": "{code}"\n},'"""
        logging.debug("Running: cppcheck...")
        utils.execute("cppcheck -q " + template + " " + self.options.path)
        logging.debug("Done")


if __name__ == "__main__":
    codestatus = CodeStatus()
    codestatus.run()
