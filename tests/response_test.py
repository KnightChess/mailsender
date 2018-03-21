import unittest
from response import *

class TestResponse(unittest.TestCase):

    def test_basic_response_01(self):
        resp = basic_response(SUCCESS)
        self.assertEqual(resp["code"], SUCCESS)
        self.assertEqual(resp["msg"], defaultCodeMsg[SUCCESS])
        self.assertEqual(resp["data"], None)

    def test_basic_response_02(self):
        resp = basic_response(ERROR)
        self.assertEqual(resp["code"], ERROR)
        self.assertEqual(resp["msg"], defaultCodeMsg[ERROR])
        self.assertEqual(resp["data"], None)

    def test_basic_response_03(self):
        resp = basic_response(-1)
        self.assertEqual(resp["code"], -1)
        self.assertEqual(resp["msg"], None)
        self.assertEqual(resp["data"], None)

if __name__ == '__main__':
    unittest.main()