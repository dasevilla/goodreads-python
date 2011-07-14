import unittest
import basetest


class TestShelfs(basetest.BaseTestCase):

    TEST_USER_ID = "GOODREADS_USER_ID"
    TEST_SHELF_NAME = "to-read"

    def test_user_shelves(self):
        shelfs = self.client.user_shelves(self.TEST_USER_ID)
        self.assertIsNotNone(shelfs)

    def test_get_shelf(self):
        books = self.client.get_shelf(self.TEST_USER_ID, self.TEST_SHELF_NAME)
        self.assertIsNotNone(books)


if __name__ == '__main__':
    unittest.main()
