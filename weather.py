import json
import urllib.request

def post_slack():
    REQUEST_URL = # ここに調べたい地域の Yhaoo 気象情報 API のリクエスト URL を記入してください
    WEB_HOOK_URL = # ここに取得した Slack Webhook URL を記入してください

    reqg = urllib.request.Request(REQUEST_URL)
    with urllib.request.urlopen(reqg) as res:
        response = res.read()

    response = response.decode()

    d = json.loads(response)

    rainfall = d['Feature'][0]['Property']['WeatherList']['Weather'][0]['Rainfall']

    payliad_d = {
        'text': '現在の降水強度は {} mm/h です。'.format(rainfall)
    }

    data = json.dumps(payliad_d).encode('utf-8')

    reqp = urllib.request.Request(WEB_HOOK_URL, data, method='POST')
    with urllib.request.urlopen(reqp) as res:
        body = res.read().decode('utf-8')
