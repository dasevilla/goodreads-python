import unittest

from goodreads import GoodReadsClient

class BaseTestCase(unittest.TestCase):

    GOODREADS_API_KEY = "GOODREADS_API_KEY"
    GOODREADS_API_SECRET = "GOODREADS_API_SECRET"

    def setUp(self):
        self.assertIsNotNone(self.GOODREADS_API_KEY)
        self.assertIsNotNone(self.GOODREADS_API_SECRET)
        
        self.client = GoodReadsClient(
            self.GOODREADS_API_KEY,
            self.GOODREADS_API_SECRET)

    def tearDown(self):
        self.client = None
