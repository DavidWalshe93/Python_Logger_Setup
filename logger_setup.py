# David Walshe
# 06/03/2019
# Credit to: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# Simple function to create a custom logger with file handlers, formatters and filters from a yaml config file

import logging.config
import os
import yaml


def setup_logging(
    # Default path needs to be placed in your root project directory.
    default_path='logging_config.yaml',
    default_level=logging.INFO,
    # Setup an environment variable to your logger_config.yaml path and use it here
    env_key='LOG_CONFIG',
    append=True
):
    """Setup logging configuration

    """
    path = default_path
    config = None
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    # Setup so every time the code is run the logger deletes the last log
    if not append:
        log_name = config["handlers"]["info_file_handler"]["filename"]
        with open(log_name, "w") as fh:
            pass
        log_name = config["handlers"]["error_file_handler"]["filename"]
        with open(log_name, "w") as fh:
            pass

