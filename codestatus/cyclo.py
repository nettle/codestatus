"""
Cyclomatic complexity

Requires: cyclo or cyclo 2.0

Download from:
* https://maultech.com/chrislott/resources/cmetrics/
* https://github.com/orbitcowboy/cyclo-2.0
* https://github.com/forslund/cyclo

Run:

    mcstrip <file> | cyclo -c

"""

import logging

import utils


class Cyclo:
    """FIXME"""
    def __init__(self):
        """FIXME"""
        logging.debug("Cyclo: init")

    def run(self):
        """FIXME"""
        logging.debug("Cyclo: running...")
        # logging.debug("Running: sw_metrics...")
        # utils.execute("sw_metrics " + self.options.path)
