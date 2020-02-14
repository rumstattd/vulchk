import click

from vulchk.getnistdata import get_gzipped_json
from vulchk.process import parse

@click.command()
@click.option("--name", '-n', default=None, multiple=True, required=True, help="Name of the product to search for")
@click.option("--version", '-v', multiple=True, help="Version of the product to search for")
@click.option("--url", '-u', default='https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2019.json.gz', show_default=True, help="URL to get NIST data from")
def cli(name, version, url):
    data = get_gzipped_json(url)
    # Currently printing all data in NIST file
    parse(data)
