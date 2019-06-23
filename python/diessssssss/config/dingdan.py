#

import requests
import sys
sys.path.append(r'D:\work\untitled\diessssssss')

from diessssssss.data import dingdanshuju

class Ding_dnag():
    def Ds_mingxi(self,num):
        url = 'https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'

        heard = {
                 'Content-Type': "application/json",
                 'x-dealer-code': "2100005",
                 'x-position-code': "D_PO_1028",
                 'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
                 'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                 'x-user-code': "dhxc1u",
                 'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
                 'cache-control': "no-cache",
                 'Postman-Token': "90dfc777-dcee-4faa-a771-509ed5358a2d"
                }

        paylode = '{\r\n \"pageNum\":\"%s\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"R2100003181001390\"\r\n }\r\n}'%(num)

        res = requests.post(url=url,headers=heard,data=paylode)
        print(res)

        return res.json()


if __name__ =='__main__':
    # for num in dingdanshuju.shuju():
    #     print(num)

    print(Ding_dnag().Ds_mingxi(1))





