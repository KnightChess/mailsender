import unittest

from mail import send


class MailTest(unittest.TestCase):

    # send mail without from_alias and html parameter
    def test_send_01(self):
        try:
            send('test@vimsucks.com', 'title', 'content')
        except Exception:
            self.fail('send function raised unexpected exception')

    # send mail without html parameter
    def test_send_02(self):
        try:
            send('test@vimsucks.com', 'title', 'content', 'test')
        except Exception:
            self.fail('send function raised unexpected exception')


    # send mail with undefined account
    def test_send_03(self):
        self.assertRaises(KeyError, send, 'test@vimsucks.com', 'title', 'content', 'not_exists')

    # send mail with all parameters
    def test_send_04(self):
        try:
            send('test@vimsucks.com', 'title', '<h1>233</h1>', 'test', True)
        except Exception:
            self.fail('send function raised unexpected exception')
