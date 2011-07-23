import unittest

import basetest
import config


class TestShelfs(basetest.BaseTestCase):

    def test_user_shelves(self):
        shelfs = self.client.user_shelves(config.TEST_USER_ID)
        self.assertIsNotNone(shelfs)

    def test_get_shelf(self):
        books = self.client.get_shelf(config.TEST_USER_ID,
            config.TEST_SHELF_NAME)
        self.assertIsNotNone(books)


if __name__ == '__main__':
    unittest.main()
