from wxpusher import WxPusher

APP_TOKEN = "AT_6xOCcOPd4vfVETlGAvcZ36jcTNCvLx3e"
UID = "UID_Jcp4BjUmmbHPzMjsXaO4gdgjoX8J"

message = "⏰ 记得打卡！"

WxPusher.send_message(
    content=message,
    uids=[UID],
    token=APP_TOKEN
)
