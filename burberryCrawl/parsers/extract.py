import re


_re_non_spaces = re.compile(u'[^\s]+|\n', flags=re.UNICODE)
_re_norm_CR = re.compile(u'(?:\s*\n\s*)+', flags=re.UNICODE)


def normalize_spaces(value):
    cleared_value = u' '.join(_re_non_spaces.findall(value))
    return _re_norm_CR.sub(u'\n', cleared_value).strip()


def parser_url_images(urls):
    parsed_urls = []
    for url in urls:
        if 'http' in url:
            url = url.split("'")[1]
        else:
            split_url = url.split(',')[1].strip().split(' ')[0]
            url = f"http:{split_url}"
        parsed_urls.append(url)

    return parsed_urls


def parser_description(descriptions):
    return ','.join(descriptions)
