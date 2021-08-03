import unittest
from day13_1 import *
class testOne(unittest.TestCase):
    def testjian(self):
        a = 5
        b = 3
        c = 2
        day = Calc()
        sum = day.subs(a,b)
        self.assertEqual(c,sum)
        pass

    def testcheng(self):
        a = 5
        b = 3
        c = 24
        day = Calc()
        sum = day.multi(a,b)
        self.assertEqual(c,sum)
        pass

    def testjian(self):
        a = 6
        b = 3
        c = 2
        day = Calc()
        sum = day.devision(a,b)
        self.assertEqual(c,sum)
        pass