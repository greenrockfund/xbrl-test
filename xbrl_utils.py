""" XBRL utilities """
import json
import logging

from xbrl.cache import HttpCache
from xbrl.instance import XbrlParser, XbrlInstance

# just to see which files are downloaded
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_xbrl(xbrl_file):
    """ Call to NBB API /authentic/xxx/references 
    Args
        - xbrl_file
    Returns
        - parsed dict
    """

    cache: HttpCache = HttpCache('./cache')
    cache.set_headers({'From': 'seb@greenrock.be', 'User-Agent': 'py-xbrl/2.1.0'})
    parser = XbrlParser(cache)

    schema_url = "https://www.nbb.be/doc/ba/xbrl/Taxo2019bis/files/pfs-full-2020-02-01.xsd"
    inst: XbrlInstance = parser.parse_instance(schema_url)

    # # Parse file
    # xbrl_parser = XBRLParser()
    # xbrl = xbrl_parser.parse(open(xbrl_file))


    # # Serialize object
    # gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20221231", context="current", ignore_errors=0)

    # serializer = GAAPSerializer()
    # result = serializer.dump(gaap_obj)

    logger.debug(f'inst: {inst}')
