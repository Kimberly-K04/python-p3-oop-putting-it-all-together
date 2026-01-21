#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    def __repr__(self):
        return f"<Book '{self.title}' ({self.page_count} pages)>"

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    def read(self, pages):
        """Read a number of pages, updates current page, logs progress"""
        if pages < 0:
            raise ValueError("Pages read cannot be negative")
        old_page = self.current_page
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        self.read_history.append((old_page, self.current_page))
        print(f"You read {self.current_page - old_page} pages. Now at page {self.current_page}.")

    def bookmark(self):
        print(f"Bookmark set at page {self.current_page}")

    def reset(self):
        """Reset reading progress"""
        self.current_page = 0
        self.read_history.clear()
        print(f"Progress reset for '{self.title}'")

        