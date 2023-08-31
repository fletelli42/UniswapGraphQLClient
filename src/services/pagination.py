# services/pagination.py

class Paginator:

    def __init__(self, items, items_per_page=10):
        self.items = items
        self.items_per_page = items_per_page

    def get_page(self, page_number):
        start_index = (page_number - 1) * self.items_per_page
        end_index = start_index + self.items_per_page

        return self.items[start_index:end_index]
