import json
import logging
import unittest


class TestCaseBase(unittest.TestCase):
    json_path = ""
    LOGGER = logging.getLogger(__name__)

    def setUp(self) -> None:
        print("We are in the setUp method!!")
        self.LOGGER.info("We are in the setUp method!!")

    def tearDown(self) -> None:
        print("We are in the tearDown method!!")
        self.LOGGER.info("We are in the tearDown method!!")

    def json_loader(self, filename):
        with open(filename, 'r') as f:
            print(filename)
            data = json.load(f)
        return data
