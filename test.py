
import datetime
import requests
testeddate = '2022-04-11 17:26:18'
dt_obj = datetime.datetime.strptime(testeddate, '%Y-%m-%d %H:%M:%S')
dt_str = datetime.datetime.strftime(dt_obj, '%d-%m-%Y %H:%M:%S')
print(dt_str)


base_url = 'http://192.168.1.8:5000'

url = base_url + ('/auth/get-uid?id=2')

r = requests.get(url).json()

print(r)
