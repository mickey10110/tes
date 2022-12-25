from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import configparser
import os
import requests



app = Flask(__name__)

handler = WebhookHandler('9188265750e78cf498b5cd5404b08425')
line_bot_api = LineBotApi('T830BxZhlnr9AB8LmDZ9WvbEa1U2F7ri8Q9P+8Ruopg7B7uGi6KHQCV1S019QfktArX/EFWb0ZgunP9HJzl+hqf/aUXnkSZWXT9BIbn/0BOxkIOdCXf9TezGl9Qb/0n4+SsAPBSuBS8wSJzLhEIIWgdB04t89/1O/w1cDnyilFU=')
line_bot_api.push_message('Ub7bf655b5badc48935203e81a4a6a92c', TextSendMessage(text='輸入個位數字'))
    
@app.route('/callback', methods= ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text = True)
    app.logger.info("Request body: " + body)
    print(body)

    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
     
      
    
    mtext=event.message.text
    if len(mtext)==1:
      if mtext.isdigit():
                 if (int(mtext)%2)==0:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入末兩位數字'))
                    
                 
                 else:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此數不是2500的倍數'))
        
             
                      
      else:
                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入數字'))
     
    elif len(mtext)==2:
      if mtext.isdigit():
                 if (int(mtext)%4)==0:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入末三位數字'))
                    
                 
                 else:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此數不是2500的倍數'))
        
             
                      
      else:
                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入數字'))
    
    elif len(mtext)==3:
      if mtext.isdigit():
                 if int(mtext)%250)==0:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入末四位數字'))
                    
                 
                 else:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此數不是2500的倍數'))
        
             
                      
      else:
                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入數字'))
    
    elif len(mtext)==4:
      if mtext.isdigit():
                 if (int(mtext)%2500)==0:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此數字是2500的倍數 可重新輸入下一個數的個位數字'))
                    
                 
                 else:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此數不是2500的倍數'))
        
             
                      
      else:
                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請輸入數字'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='輸入錯誤 請重新輸入數字'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
