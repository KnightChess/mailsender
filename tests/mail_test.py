import unittest

from mail import send


class MailTest(unittest.TestCase):

    def test_send_01(self):
        try:
            send('test@vimsucks.com', 'title', 'content')
        except Exception:
            self.fail('send function raised unexpected exception')
