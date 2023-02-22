#!/usr/bin/env python3

import logging

LOGFILE = "out.put"

K4_IP="192.168.147.21"

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

logging.basicConfig(filename=LOGFILE)

# so my_logger is set to debug level, while generic logging stays at Warning.
# The output of this short test is:
#
# WARNING:root:watch out
# WARNING:MyLogger:watch you 2
# DEBUG:MyLogger:Telnet2 to: 192.168.147.21
#


logging.warning('watch out')
my_logger.warning('watch you 2')

#next line does nothing, because it is below generic logging level
logging.debug("Telnet to: %s", K4_IP)

#but this one will go out.
my_logger.debug("Telnet2 to: %s", K4_IP)
