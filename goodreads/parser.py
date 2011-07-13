import logging
from xml.dom import minidom, Node
from xml.parsers.expat import ExpatError, ErrorString


class GoodReadsParser(object):

    def parse_result(self, url_handler):
        try:
            goodreads_dom = minidom.parse(url_handler)
            return goodreads_dom
        except ExpatError, e:
            logging.error("XML Error: %s line: %d offset: %d" % (
                ErrorString(e.code), e.lineno, e.offset))
            return None

    def get_text(self, element):
        value = ""

        for text in element.childNodes:
            try:
                value += text.data
            except AttributeError:
                logging.error("get_text() error: " + text.toxml())
                raise

        if value:
            return value.strip()
        else:
            return None

    def parse_books(self, url_handler):
        goodreads_dom = self.parse_result(url_handler)
        books = []
        for book_element in goodreads_dom.getElementsByTagName("book"):
            book = self.handle_book(book_element)
            if book:
                books.append(book)
        return books

    def handle_book(self, book_element):
        book = {}
        for child_node in book_element.childNodes:
            value = ""

            if child_node.nodeType == Node.TEXT_NODE:
                continue
            elif child_node.nodeName == "authors":
                value = self.handle_authors(child_node)
            elif  child_node.nodeName == "shelves":
                logging.info("found shelves")
                continue
            else:
                value = self.get_text(child_node)

            book[child_node.nodeName] = value
        return book

    def parse_shelfs(self, url_handler):
        goodreads_dom = self.parse_result(url_handler)
        shelfs = []
        for shelf_element in goodreads_dom.getElementsByTagName("user_shelf"):
            shelf = self.handle_shelf(shelf_element)
            if shelf:
                shelfs.append(shelf)
        return shelfs

    def handle_shelf(self, shelf_element):
        shelf = {}
        for child_node in shelf_element.childNodes:
            value = ""

            if child_node.nodeType == Node.TEXT_NODE:
                continue
            else:
                value = self.get_text(child_node)

            shelf[child_node.nodeName] = value
        return shelf

    def handle_authors(self, authors_element):
        authors = []
        for child_node in authors_element.childNodes:
            author = self.handle_author(child_node)
            if author:
                authors.append(author)
        return authors

    def handle_author(self, author_element):
        author = {}
        for child_node in author_element.childNodes:
            value = ""

            if child_node.nodeType == Node.TEXT_NODE:
                continue
            else:
                value = self.get_text(child_node)

            author[child_node.nodeName] = value
        if author:
            return author
        else:
            return None
