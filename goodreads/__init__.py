import logging
import urllib

from goodreads.parser import GoodReadsParser


class GoodReadsClient(object):

    BASE_URL = "http://www.goodreads.com/"
    DEFAULT_PAGE_SIZE = 200

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.parser = GoodReadsParser()

    def unauthorized_request(self, base_url, query_params):
        if "key"not in query_params:
            query_params["key"] = self.key
        if "per_page" not in query_params:
            query_params["per_page"] = self.DEFAULT_PAGE_SIZE

        params = []
        for k, v in query_params.iteritems():
            if v is not None:
                params.append("%s=%s" % (k, v))
        url = "%s?%s" % (base_url, "&".join(params))
        logging.info("Making request to %s" % url)
        url_handler = urllib.urlopen(url)
        return url_handler

    def parse_result(self, url_handler):
        return self.parser.parse_result(url_handler)

    def user_shelves(self, user_id):
        url = "%sshelf/list.xml" % self.BASE_URL
        query_params = {
            "user_id": user_id,
        }

        url_handler = self.unauthorized_request(url, query_params)
        return self.parser.parse_shelfs(url_handler)

    def get_shelf(self, user_id, shelf_name):
        url = "%sreview/list.xml" % self.BASE_URL
        query_params = {
            "id": user_id,
            "shelf": shelf_name,
            "v": 2,
        }

        url_handler = self.unauthorized_request(url, query_params)
        return self.parser.parse_books(url_handler)
