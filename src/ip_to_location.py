import json
import urllib.request

GEO_IP_API_URL = 'http://ip-api.com/json/'

with open('data.txt') as f:
    lines = f.readlines()

checked = []
for line in lines:
    if " - - " in line:
        ip = line.split(" - - ")[0]
        if ip not in checked:
            checked.append(ip)
            req = urllib.request.Request(GEO_IP_API_URL + ip)
            response = urllib.request.urlopen(req).read()
            json_response = json.loads(response.decode('utf-8'))
            print(f"IP : {ip} ,ISP {json_response['isp']}, Country: {json_response['country']}")
