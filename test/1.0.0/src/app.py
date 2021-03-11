import socket
import asyncio
import time
import random
import json
import requests

from walkoff_app_sdk.app_base import AppBase


class HelloAnna(AppBase):
    """
    An example of a Walkoff App.
    Inherit from the AppBase class to have Redis, logging, and console logging set up behind the scenes.
    """
    __version__ = "1.0.0"
    app_name = "hello_anna"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    async def hello_world(self, message):
        """
        Returns Hello World from the hostname the action is run on
        :return: Hello World from your hostname
        """
        my_message = f"Hello World from {message} in workflow {self.current_execution_id}!"

        # This logs to the docker logs
        self.logger.info(my_message)

        return my_message

if __name__ == "__main__":
    asyncio.run(HelloAnna.run(), debug=True)
