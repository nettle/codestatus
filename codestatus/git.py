"""
Git statistics

Requires: git (version 2.17.1?)

Statistics:
- Number of commits
- Number of contributors
- Number of commits per day, week, month, year
- Number of contributors per day, week, month, year
"""

import ast
import logging
import os

import utils


class Git:
    """FIXME"""
    def __init__(self):
        """FIXME"""
        logging.debug("Git: init")

    def run(self):
        """FIXME"""
        logging.debug("Git: running...")
        if not utils.available("git"):
            logging.error("Git: git is not available")
            return False
        else:
            logging.debug("Git: version: %s", utils.execute("git --version"))
        if not os.path.isdir(".git"):
            logging.error("Git: no git files found")
            return False
        form = "{\"d\": \"%cd\", \"e\": \"%ae\"},"
        command = "git log --format=format:'{form}' --date=short".format(form=form)
        logging.debug("Git: command: %s", command)
        log = utils.execute(command)
        logging.debug("Git: log: %s", log[0:50])
        # log = "{\"h\": 1},"
        logging.debug("Git: parsing...")
        data = ast.literal_eval("[" + log + "]")
        logging.debug("Git: OK")
        logging.debug("Git: data[0]: %s", data[0])
        logging.debug("Git: len: %s", len(data))
