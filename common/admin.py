from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def get_list_display(self, request, related_geo=None):
        items = ['id', 'idx', 'name', 'created_on',
                 'modified_on', "is_obsolete"]
        if related_geo:
            items.insert(3, related_geo)
        return items
