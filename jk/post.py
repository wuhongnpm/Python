import requests
'''
param =  {"timestamp":"1618972691000","sign":"FFB94DE4131F385BA00D9B5F83352ECC","eqType":"20000","eqSn":"CCL7000F24AL02B2018110153","eqCode":"CCL7000F24AL02B2018110153"}
r=requests.post("https://uscp.api.test.cclyun.cn/api/version/getAppStoreList",params=param)

print(r.status_code)
print(r.content)
print(r.headers)
print(r.json())
print(r.url)
print(r.encoding)
print(r.cookies)
print(r.raw)
print(r.text)
'''

'''
//dict参数
url = 'https://uscp.api.test.cclyun.cn/api/version/getAppStoreList'
payload = {"timestamp":"1618972691000","sign":"FFB94DE4131F385BA00D9B5F83352ECC","eqType":"20000","eqSn":"CCL7000F24AL02B2018110153","eqCode":"CCL7000F24AL02B2018110153"}
response = requests.post(url=url,data=payload)
print(response.text)
'''

import json
'''
//json参数
url = 'https://uscp.api.test.cclyun.cn/api/version/getAppStoreList'
payload = {"timestamp":"1618972691000","sign":"FFB94DE4131F385BA00D9B5F83352ECC","eqType":"20000","eqSn":"CCL7000F24AL02B2018110153","eqCode":"CCL7000F24AL02B2018110153"}
data_json = json.dumps(payload)
respone = requests.post(url=url,json=data_json)
print(respone.text)
'''

'''
url = 'https://uscp.api.test.cclyun.cn/api/version/getAppStoreList'
payload = {"timestamp":"1618972691000","sign":"FFB94DE4131F385BA00D9B5F83352ECC","eqType":"20000","eqSn":"CCL7000F24AL02B2018110153","eqCode":"CCL7000F24AL02B2018110153"}
response = requests.post(url=url,headers=payload,verify=False)
print(response.text)
print(response.json())
'''




