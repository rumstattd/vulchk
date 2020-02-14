from gzip import decompress
from json import loads
from requests import get

def get_gzipped_json(url):
    return loads(decompress(get(url).content))
