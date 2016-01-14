import unittest
import nose2


def test_b():
    assert 'b' == 'b'

def test_check():
    assert 'c'== 'c'


class Test(unittest.TestCase):

    def test_fast(self):
       self.assertTrue (1)


    def test_slow(self):
       self.assertFalse (0)
   
   