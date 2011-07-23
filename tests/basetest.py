import unittest

from goodreads import GoodReadsClient
import config


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.assertIsNotNone(config.GOODREADS_API_KEY)
        self.assertIsNotNone(config.GOODREADS_API_SECRET)

        self.client = GoodReadsClient(
            config.GOODREADS_API_KEY,
            config.GOODREADS_API_SECRET)

    def tearDown(self):
        self.client = None
