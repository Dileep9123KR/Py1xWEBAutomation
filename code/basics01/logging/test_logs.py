# logging -> Capture details for debugging and show the user details about execution of programs
# Displays warning errors when a failure occurs to the user
# Information to the users, Errors, Critical Errors to users

import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    # Different logging we have are shown below;
    LOGGER.info("This is Information logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical logs")
