import requests

SEND_KEY = "你的SendKey"

url = f"https://sctapi.ftqq.com/{SCT320719TkhUywucvOrY5IA1q3MXshnZU}.send"

data = {
    "title": "打卡提醒",
    "desp": "⏰ 记得打卡！"
}

requests.post(url, data=data)
