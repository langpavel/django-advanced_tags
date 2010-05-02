from datetime import datetime

from django.db import models


class TagManager(models.Manager):

    def __init__(self, *args, **kwargs):
        self.restrict_date = kwargs.get('restrict_date', False)
        if self.restrict_date:
            del kwargs['restrict_date']
        super(TagManager, self).__init__(*args, **kwargs)

    def get_query_set(self):
        qs = super(TagManager, self).get_query_set()
        if self.restrict_date:
            qs = qs.filter(valid_from__lte=datetime.now, \
                valid_to__gte=datetime.now)
        return qs


class TaggedItemManager(models.Manager):
    pass
