import json
from urllib.request import urlopen
def getCountry(idAddress):
    response = urlopen("http://freegeoip.net/"+idAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")
print(getCountry("50.78.253.58"))
