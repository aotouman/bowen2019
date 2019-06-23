#!/use/bin/python
#-*- conding:utf-8 -*-

from  diessssssss.config.dingdan import Ding_dnag
from  diessssssss.data.dingdanshuju import shuju
import unittest

class D_dan(unittest.TestCase):
    ss = shuju()
    def test_1(self):

        aa = Ding_dnag().Ds_mingxi(int(self.ss[1][0]))
        # print(aa)

        #一下一句是断言，根据所测试的接口数据来写
        self.assertEqual(aa['errMsg'],'该订单号对应的订单不存在！')
    def test_2(self):
        aa = Ding_dnag().Ds_mingxi(self.ss[2][0])
        # print(aa)
        self.assertNotIn('该订单号对应的订单不存在！',aa)

if __name__ == '__main__':
    unittest.main()     # unittest.main()    会自动检测继承了Test Case 类的类中的所有test开头的结果
    #将所有的test开头的文件都当作用例执行一遍
    #执行顺序是按照test后的字符在asca码中的位置排序








