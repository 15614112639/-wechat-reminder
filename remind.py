from wxpusher import WxPusher

APP_TOKEN = "AT_6xOCcOPd4vfVETlGAvcZ36jcTNCvLx3e"
TOPIC_ID = 43605

result = WxPusher.send_message(
    content="⏰ 记得打卡！",
    topic_ids=[TOPIC_ID],
    token=APP_TOKEN
)
print(result)
