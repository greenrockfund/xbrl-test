""" Unit tests """
import json
import logging
import unittest

from xbrl_utils import parse_xbrl

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestNbbXbrl(unittest.TestCase):

    def test_parse_xbrl(self):
        """ Test parse_xbrl
        python -m unittest test.TestNbbXbrl.test_parse_xbrl
        """
        response = parse_xbrl('nbb_prod_data/2022-20067257.xbrl')
        #logger.debug(f'response:{response}')
        logger.debug(f'api_response:{json.dumps(response, indent=3)}')

if __name__ == '__main__':
    unittest.main()
