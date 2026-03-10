from wxpusher import WxPusher
import datetime

APP_TOKEN = "AT_6xOCcOPd4vfVETlGAvcZ36jcTNCvLx3e"
UID = "UID_Jcp4BjUmmbHPzMjsXaO4gdgjoX8J"

WxPusher.send_message(
    "⏰ 记得打卡！",
    uids=[UID],
    token=APP_TOKEN
)
