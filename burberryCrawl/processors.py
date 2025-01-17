from pytz import unicode
from six import string_types
from w3lib.html import remove_tags

from burberryCrawl.parsers.extract import normalize_spaces


class DefaultInputProcessor:

    def __call__(self, values):
        try:
            new_values = []
            for value in values:
                value = self.__clear_value(value)
                if value is not None and value != u'':
                    new_values.append(value)
            return new_values
        except:
            return values

    @staticmethod
    def __clear_value(value):
        if isinstance(value, string_types):
            unicode = lambda s: str(s)
            try:
                cleared_value = unicode(remove_tags(value))
                return normalize_spaces(cleared_value)
            except:
                return value
        else:
            return value


class DefaultOutputProcessor(object):

    def __call__(self, values):
        try:
            if isinstance(values, string_types):
                return unicode(values).strip()
            elif len(values) > 1:
                return u' '.join(unicode(v).strip() for v in values)
            else:
                return values[0]
        except:
            return values


class TakeLast(object):

    def __call__(self, values):
        for value in reversed(values):
            if value is not None and value != '':
                return value