import unittest

import test_dublinBikes


class Test_dublinbikesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = test_dublinBikes.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to test_dublinBikes', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
