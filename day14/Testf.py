from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from bank1 import *
ban = bank_user
ban.account = 110006
ban.username = '大佬1'

# "123456","中国","北京","沟里","110",10000028


da = [
    [11000,True],
[11001,False],
[56525215,True],
[73647629,True]
]
da1 = [[4],[4]]
da3=[[22000,"xx","123","asd","qwe","asdzx","626",6000,2],
[22001,"xa","123","asd","qwe","asdzx","626",6001,2],
[22002,"xs","123","asd","qwe","asdzx","626",6002,2],
[22003,"xd","123","asd","qwe","asdzx","626",6003,2]
     ]

@ddt
class Testf(TestCase):
    @data(*da)
    @unpack
    def testbooleanuser(self,a,b):
        self.assertEqual(booleanuser(a),b)
        pass


    @data(*da3)
    @unpack
    def testbank_addUser(self, a,b,c,d,e,f,g,h,u):
        self.assertEqual(bank_addUser(a,b,c,d,e,f,g,h), u)

