import re


_re_non_spaces = re.compile(u'[^\s]+|\n', flags=re.UNICODE)
_re_norm_CR = re.compile(u'(?:\s*\n\s*)+', flags=re.UNICODE)


def normalize_spaces(value):
    cleared_value = u' '.join(_re_non_spaces.findall(value))
    return _re_norm_CR.sub(u'\n', cleared_value).strip()

