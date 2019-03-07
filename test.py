# David Walshe
# 06/03/2019
# Simple test for checking logging config setup

import logger_setup
import logging

logger_setup.setup_logging()
logger = logging.getLogger(__name__)
logger.debug("DEBUG")
logger.info("INFO")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")

