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
line_bot_api.push_message('Ub7bf655b5badc48935203e81a4a6a92c', TextSendMessage(text='輸入一個數字'))
    
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
    userid=event.source.user_id
    sql_cmd="select * from users where uid='" + userid + "'"
    query_data= db.engine.execute(sql_cmd)
    
    if len(list(query_data))==0:
        sql_cmd = "insert into users (uid, state, digit3) values('" + userid + "', 'no', 'no');"
        db.engine.execute(sql_cmd)
    else:
        query_data= db.engine.execute(sql_cmd)
        listdata = list(query_data)[0]
        mode= listdata[2]
        digit3= listdata[3]
    
    
    mtext=event.message.text
    if len(mtext)==3 and mtext.isdigit():
        show3digit(event, mtext,userid)


def show3digit(event, mtext,userid):
    try:
         


        prizelist=[23456789]
         
        prize6list1 = [12345678]
        prize6list2 =[23456789]
 
         

        if mtext in prizelist:
            message='符合特別獎或特獎後三碼 請繼續輸入前五碼'
            sql_cmd="update users set state='special', digit3='"+ mtext + "'where uid='"+userid +"'"
            db.engine.execute(sql_cmd)

        elif mtext in prize6list1:
            message='至少中六獎 請繼續輸入前五碼'
            sql_cmd="update users set state='head', digit3='"+ mtext + "'where uid='"+userid +"'"
            db.engine.execute(sql_cmd)
        elif mtext in prize6list2:
            message = '恭喜中六獎'
        else:
            message= '可惜 未中獎 請輸入下一組後三碼'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='讀取時發生錯誤'))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
