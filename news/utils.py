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
