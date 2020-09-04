import requests
i


def iost(year,category):
    params = {
      'year' : 2019,
      'category' : 'chemistry'
    }

    iostCall = "http://api.nobelprize.org/v1/prize.json"
    iostCallJson = requests.get(iostCall, params=params).json()
    iostOut = iostCallJson
    update.message.reply_text(iostOut)

iost(year='1983', category='physics')