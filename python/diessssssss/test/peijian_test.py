#!/use/bin/python
#-*- conding:utf-8 -*-


from diessssssss.config.peijian import P_chaxun
from diessssssss.data.P_shuju import PJ_shuju
import unittest

class p_mingxi(unittest.TestCase):

    pj = PJ_shuju()
    def test_1(self):
        pp = P_chaxun().pei_jian(self.pj[1][1])
        self.assertEqual(pp['data']['pageNum'],3)
    def test_2(self):
        pp = P_chaxun().pei_jian(self.pj[2][1])
        self.assertEqual(pp['status'],1)

if __name__ == '__main__':
    unittest.main()










