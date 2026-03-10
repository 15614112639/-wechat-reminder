import requests

SEND_KEY = "SCT320719TkhUywucvOrY5IA1q3MXshnZU"

url = f"https://sctapi.ftqq.com/{SEND_KEY}.send"

data = {
    "title": "打卡提醒",
    "desp": "⏰ 记得打卡！"
}

requests.post(url, data=data)
