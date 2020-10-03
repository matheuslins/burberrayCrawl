import re


_re_non_spaces = re.compile(u'[^\s]+|\n', flags=re.UNICODE)
_re_norm_CR = re.compile(u'(?:\s*\n\s*)+', flags=re.UNICODE)


def normalize_spaces(value):
    cleared_value = u' '.join(_re_non_spaces.findall(value))
    return _re_norm_CR.sub(u'\n', cleared_value).strip()


def parser_url_images(urls):
    parsed_urls = []
    for url in urls:
        url_spplited = url.split(',')[1].strip().split(' ')[0]
        parsed_urls.append(f"http:{url_spplited}")
    return parsed_urls


def parser_description(descriptions):
    return ','.join(descriptions)
