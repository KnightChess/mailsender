import unittest

suite = unittest.TestLoader().discover('tests', '*_test.py')
unittest.TextTestRunner(verbosity=2).run(suite)