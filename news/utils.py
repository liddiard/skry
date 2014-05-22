import json
import datetime
from time import mktime

from django.utils.timezone import now as django_now


# encode datetimes in json
class DatetimeEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

def pretty_list_from_queryset(items):
    if len(items) < 2:
        return str(items.first())
    else:
        return ", ".join([str(i) for i in items if i != items.last()]) + \
               " and " + str(items.last())
