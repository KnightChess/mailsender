import unittest
from response import *

class TestResponse(unittest.TestCase):
    def test_basic_response_01(self):
        resp = basic_response(1)
        self.assertEqual(resp['msg'], True)

    def test_basic_response_02(self):
        resp = basic_response(2)
        self.assertEqual(resp['msg'], True)

    def test_basic_response_03(self):
        self.assertRaises(ValueError, basic_response, 'z')

if __name__ == '__main__':
    unittest.main()