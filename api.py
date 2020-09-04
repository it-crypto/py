import requests
import pprint


parameters = {
    "year":1983,
    "category": "physics"
}
r=requests.get("http://api.nobelprize.org/v1/prize.json",params=parameters)
#print(r.status_code) # it is used to check whether the request is successful or not
#print(r.headers['content-type']) # it says what type of file it is.
#print(r.json)
pprint.pprint(r.json()['prizes'])# n print first file in json format.

firstname =r['laureates']['firstname']
print(firstname)