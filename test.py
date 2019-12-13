import requests

TOKEN = '775904736:AAEREmJL53OsDxrWKdjOs0lM2bR02IWdq4w'
CHAT_ID = '90569499'

message = 'This\n is \n a \n test.'
query = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + message
r = requests.get(query)
result = r.json()
api_result = result.get('ok')
print(api_result)