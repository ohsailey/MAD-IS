import os
import __init__
import unittest
import tempfile

class ISTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, __init__.app.config['DATABASE'] = tempfile.mkstemp()
        __init__.app.config['TESTING'] = True
        self.app = __init__.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(__init__.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()