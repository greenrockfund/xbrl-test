""" XBRL utilities """
import json
import logging

from xbrl.cache import HttpCache
from xbrl.instance import XbrlParser, XbrlInstance

# just to see which files are downloaded
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#https://py-xbrl.readthedocs.io/en/latest/usage.html#offline
cache: HttpCache = HttpCache('./cache')
cache.set_headers({'From': 'seb@greenrock.be', 'User-Agent': 'py-xbrl/2.1.0'})
parser = XbrlParser(cache)


def parse_xbrl(xbrl_file):
    """ Call to NBB API /authentic/xxx/references 
    Args
        - xbrl_file
    Returns
        - parsed dict
    """

    # Online
    #schema_url = "https://www.nbb.be/doc/ba/xbrl/Taxo2019bis/files/pfs-full-2020-02-01.xsd"
    #inst: XbrlInstance = parser.parse_instance(schema_url)

    # Offline
    schema_path = "./taxonomy/be_fr_pfs_ci_2020_02_01/pfs-2020-02-01-reference.xml"
    inst: XbrlInstance = parser.parse_instance(schema_path)

    logger.debug(f'inst: {inst}')
