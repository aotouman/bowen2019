import requests
from diessssssss.data.C_shuju import CX_shuju

class cha_xun():
    def ming_xi(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList"

        payload = "{\r\n \"pageNum\": 1,\r\n \"pageSize\": %s,\r\n \"queryTerms\": {\r\n  \"orderType\": \"\",\r\n  \"orderStatus\": \"\",\r\n  \"orderDelayFlag\": \"\",\r\n  \"orderNo\": \"\",\r\n  \"startReportDate\": \"\",\r\n  \"endReportDate\": \"\"\r\n }\r\n}"%(num)
        headers = {
                   'Content-Type': "application/json",
                   'x-dealer-code': "2100001",
                   'x-position-code': "D_PO_1028",
                   'x-resource-code': "pol4s_partOrder_orderList",
                   'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
                   'x-user-code': "dhxc1u",
                   'x-access-token': "d6a5abdb98fd2ee203a4ddcd7ae47d07",
                   'cache-control': "no-cache",
                   'Postman-Token': "8b2eb5f6-c89f-4c9e-beda-a536bf8a0182"
                  }

        response = requests.request("POST", url, data=payload, headers=headers)
        # print(response.text)
        return response.json()

if __name__ == '__main__':
    for i in CX_shuju():
        print(i[0])
        # cha_xun().ming_xi(10)

