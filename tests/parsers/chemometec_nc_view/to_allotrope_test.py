from pathlib import Path

from allotropy.parser_factory import Vendor
from tests.to_allotrope_test import ParserTest

VENDOR_TYPE = Vendor.CHEMOMETEC_NC_VIEW
TESTDATA = f"{Path(__file__).parent}/testdata"


class TestParser(ParserTest):
    VENDOR = VENDOR_TYPE