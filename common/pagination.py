from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):

    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200

    def get_max_page_size(self):
        return 100

    def get_paginated_response(self, data):
        """
        API response data.
        """

        return Response(OrderedDict([
            ('total_pages', self.page.paginator.num_pages),
            ('total_records', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('record_range', self.get_record_range()),
            ('current_page', self.page.number),
            ('records', data)
        ]))

    def get_record_range(self):
        """
        Range of contents in current page.
        """

        paginator = self.page.paginator
        current_page = self.page.number
        content_per_page = paginator.per_page

        if paginator.count == 0:
            range_start = 0
            range_end = 0
        else:
            range_start = content_per_page * (current_page - 1) + 1
            range_end = content_per_page * current_page

        if range_end > paginator.count:
            range_end = paginator.count

        return [range_start, range_end]
