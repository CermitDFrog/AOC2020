#!python

def iter_input(day: int):
    for line in _iter_webdata(day):
        yield line.strip('\n')

def iter_group(day: int):
    groupraw = ''
    for line in _iter_webdata(day):
        if line == '\n':
            replace = groupraw
            groupraw = ''
            yield replace
        else:
            # line = line.replace("\n", "")
            groupraw += f'{line}'
    else:
        yield groupraw


def iter_test():
    for line in _iter_file():
        yield line


def iter_group_test():
    groupraw = ''
    for line in _iter_file():
        if line == '\n':
            replace = groupraw
            groupraw = ''
            yield replace
        else:
            # line = line.replace("\n", "")
            groupraw += line
    yield groupraw


def _iter_file():
    from os import path as ospath
    from sys import path as syspath

    with open(ospath.join(syspath[0], 'testdata'), 'r') as file:
        for line in file:
            yield line

def _iter_webdata(day: int):
    import requests
    import browser_cookie3
    from io import StringIO
    cookie = browser_cookie3.chrome(domain_name='.adventofcode.com')
    inputdata = StringIO(requests.get(f'https://adventofcode.com/2020/day/{day}/input', cookies=cookie, timeout=3).text)

    for line in inputdata:
        yield line
