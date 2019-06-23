#!/use/bin/python
#-*- conding:utf-8 -*-

from diessssssss.config.chaxun import cha_xun
from diessssssss.data.C_shuju import CX_shuju
import unittest

class CX_mx(unittest.TestCase):

    bk = CX_shuju()
    def test_1(self):
        bb = cha_xun().ming_xi(int(self.bk[0][0]))
        self.assertEqual(bb['errMsg'],'处理成功')
    def test_2(self):
        bb = cha_xun().ming_xi(int(self.bk[1][0]))
        self.assertNotIn(bb['errMsg'],"大大")

if __name__ == '__main__':
    unittest.main()



















