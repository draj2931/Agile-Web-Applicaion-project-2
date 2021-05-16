import os

from werkzeug import test
from Project import app 
import unittest


class Flasktest(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(4,4)

    def test_decrement(self):
        self.assertEqual(3,4)
    def test_other(self):
        self.assertEqual(3,4)

       


if __name__ =="__main__":
    unittest.main()

