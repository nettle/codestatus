#!/usr/bin/env python

"""
CodeStatus

This script collects code metrics
FIXME: description
"""

from __future__ import print_function
import argparse
import logging
import os

import cloc
import cppcheck
import cyclo
import git
import pmccabe


CODESTATUS_EXAMPLES = """
examples:

  # "Dry run" to see commands without execution:
  codestatus ?
"""
# FIXME: examples


class CodeStatusLauncher(object):
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
                            help="Just print commands without running them")
        parser.add_argument("--log-format",
                            default="[codestatus] %(levelname)5s: %(message)s",
                            help=argparse.SUPPRESS)
        parser.add_argument("--git",
                            default=False,
                            action="store_true",
                            help="Collect Git statistics")
        parser.add_argument("--cloc",
                            default=False,
                            action="store_true",
                            help="Run cloc - Count Lines Of Code")
        parser.add_argument("--pmccabe",
                            default=False,
                            action="store_true",
                            help="Run pmccabe - Cyclomatic Complexity")
        parser.add_argument("--cyclo",
                            default=False,
                            action="store_true",
                            help="Run cyclo - Cyclomatic Complexity")
        parser.add_argument("--cppcheck",
                            default=False,
                            action="store_true",
                            help="Run cppcheck - check C/C++ code")
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
            logging.error("Specified path '%s' does not exist", self.options.path)
            exit(1)

    def run(self):
        """
        Run CodeStatus
        """
        self.parse_args()
        cwd = os.getcwd()
        try:
            logging.debug("Chdir: %s", self.options.path)
            os.chdir(self.options.path)
            if self.options.git:
                git.Git().run()
            if self.options.cloc:
                cloc.Cloc().run()
            if self.options.pmccabe:
                pmccabe.PMcCabe().run()
            if self.options.cyclo:
                cyclo.Cyclo().run()
            if self.options.cppcheck:
                cppcheck.CppCheck().run()
            logging.debug("Done")
        finally:
            logging.debug("Restoring: %s", cwd)
            os.chdir(cwd)


if __name__ == "__main__":
    codestatus = CodeStatusLauncher()
    codestatus.run()
