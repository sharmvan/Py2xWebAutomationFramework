# Logging means - Capture details, which are useful while debugging.
# and show the user details about execution of program.

# Warning to the users
# Information to the users
# Errors, Critical Errors user.

import logging  # logging is by default package


# Here we are not creating Framework structure. It's just an explanation how logs work?
def test_print_logs():  # This is a function
    # Created an instance of logger
    LOGGER = logging.getLogger(__name__)
    # Intentional Logging to user. This is how we add the logger.
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is error Logs")
    LOGGER.critical("This is Critical logs")
    assert True == True
# Note: But logs are not getting printed and Promod sir will get it checked from his end.
