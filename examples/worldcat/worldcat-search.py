import logging
import pprint

from worldcat.request.xid import xISBNRequest

from goodreads import GoodReadsClient
from goodreads.parser import GoodReadsParser


def get_books(user_id, shelf_name):
    key = "GOODREADS_API_KEY"
    secret = "GOODREADS_API_SECRET"

    goodreads_parser = GoodReadsParser()
    goodreads_client = GoodReadsClient(key, secret)

    return goodreads_client.get_shelf(user_id, shelf_name)


def book_search(isbn):
    o = xISBNRequest(rec_num=isbn, method='getMetadata')
    o.validate()
    r = o.get_response()

    return r.data["list"][0]


def main():
    goodreads_user_id = "YOUR_USER_ID"
    goodreads_shelf = "to-read"
    for book in get_books(goodreads_user_id, goodreads_shelf):
        isbn = book["isbn"]
        title = book["title"]
        goodreads_url = book["link"]

        result = book_search(isbn)
        worldcat_url = result["url"][0]

        print "%s\n\tISBN:%s\n\t%s\n\t%s" % (title, isbn, goodreads_url,
            worldcat_url)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
