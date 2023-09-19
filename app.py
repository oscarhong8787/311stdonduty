import os
import time
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設定你的Line Bot的Channel Access Token和Channel Secret
line_bot_api = LineBotApi('ZXRrAQCDdEjTyI8Mgjzal0V4MJk+BicauPinGdzAlo81MPWj8HQor49Ak6FcSLPccbDzCAt1LnA9VbHYV29/wMWgzSoh4DO5hMTG6q6lQgZ+BHdSZVWLQAcuhKiYp+fRmUUYbEemRdtny9mFeIcT2AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f4ccaa33c9aace953d7634858742c632')

# 用戶列表，用戶編號從1到36
users = list(range(1, 37))

# Line Bot的Webhook接口
@app.route("/callback", methods=['POST'])
def callback():
    # 取得HTTP請求的標頭資訊
    signature = request.headers['X-Line-Signature']

    # 取得請求內容
    body = request.get_data(as_text=True)

    try:
        # 驗證簽名是否正確
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理文字訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 取得用戶傳來的文字訊息
    user_message = event.message.text
    
    # 這裡可以加入自己的邏輯處理，根據用戶訊息回覆不同的內容
    if user_message == '你好':
        reply_message = '你好！'
    else:
        reply_message = '我不懂你在說什麼。'
    
    # 回覆用戶訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

if __name__ == "__main__":
    # 啟動Flask應用
    app.run()
