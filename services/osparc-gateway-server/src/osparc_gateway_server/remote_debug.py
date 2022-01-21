""" Setup remote debugger with Python Tools for Visual Studio (PTVSD)

"""
import logging


def setup_remote_debugging(logger: logging.Logger):
    try:
        logger.debug("Enabling attach ptvsd ...")
        #
        # SEE https://github.com/microsoft/ptvsd#enabling-debugging
        #
        import debugpy

        REMOTE_DEBUGGING_PORT = 3000
        debugpy.listen(("0.0.0.0", REMOTE_DEBUGGING_PORT))
        # debugpy.wait_for_client()

    except ImportError as err:
        raise Exception(
            "Cannot enable remote debugging. Please install debugpy first"
        ) from err

    logger.info("Remote debugging enabled: listening port %s", REMOTE_DEBUGGING_PORT)
