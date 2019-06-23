#!/use/bin/python
#-*- conding:utf-8 -*-

import requests
from diessssssss.data.P_shuju import PJ_shuju

class P_chaxun():
    def pei_jian(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/delayOrderCancelStatus/getCancelDelayOrder"

        payload = "{\r\n \"pageNum\": 3,\r\n \"pageSize\": 1,\r\n \"queryTerms\": {\r\n    \"orderNo\":\"%s\",\r\n    \"cancelStatus\":-1,\r\n    \"applyStartDate\":20180801,\r\n    \"applyEndDate\":20180909\r\n }\r\n}"%(num)
        headers = {
                   'Content-Type': "application/json",
                   'x-dealer-code': "2100001",
                   'x-position-code': "D_PO_1028",
                   'x-resource-code': "pol4s_delayOrderCancelStatus_getCancelDelayOrder",
                   'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                   'x-user-code': "dhxc1u",
                   'x-access-token': "f14c481fe946bab4712288ba80d365b0",
                   'User-Agent': "PostmanRuntime/7.15.0",
                   'Accept': "*/*",
                   'Cache-Control': "no-cache",
                   'Postman-Token': "acdc1a7b-f7f5-4a25-9671-a40346904ec5,4374afbe-29c7-432b-a428-c25f77093c19",
                   'Host': "mobileqa.dms.saic-gm.com",
                   'cookie': "dapp.sgm.com:qa:=7142731819d68a28427de15602b18ce4; fdaa0f2d854071f7f82d1c80a99830bb=adf02ffc5ea63397f0ea07c570d85acf; dapp.sgm.com:qa:=7142731819d68a28427de15602b18ce4; a689baa2b7060531c4d0be5b10aa7055=a3a54f569b14d5196ef24d5b4b890058",
                   'accept-encoding': "gzip, deflate",
                   'content-length': "172",
                   'Connection': "keep-alive",
                   'cache-control': "no-cache"
                 }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response.json()

if __name__ == '__main__':
    for i in PJ_shuju():
        # print(i[1])
        print( P_chaxun().pei_jian(10))












