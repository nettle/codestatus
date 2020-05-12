"""
Common utilities
"""

import logging
import shlex
import subprocess


def execute(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """Run shell command"""
    if type(command) is list:
        cmd = command
    else:
        cmd = shlex.split(command)
    try:
        process = subprocess.Popen(cmd, stdout=stdout, stderr=stderr)
        out, err = process.communicate()
        return out
    except KeyboardInterrupt:
        logging.error("Interrupted!")


def available(tool):
    """Return True if tool available"""
    return bool(execute("which " + tool))
