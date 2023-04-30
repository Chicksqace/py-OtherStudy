#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/5/8 20:14
# @Author : 不知天文，不知地理
# @File : dd.py
import json
import hmac
import hashlib
import base64
import time

api_blueprint = Blueprint(__name__ + '_api', __name__)
logger = get_logger(logger_type='run')


def check_sign_result(post_timestamp, post_sign):
    timestamp = round(time.time() * 1000)
    app_secret = 'ASAO7-nwDBzT1ObEo1PC6htvjHwlIBeu-4sZ7oVDQjf86EOA0DASgylZg-LIKmcL'
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(post_timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    # 校验时间戳/sign
    if (timestamp - int(post_timestamp) < 36000000 or (int(post_timestamp) - timestamp) < 3600000) and sign == post_sign:
        return True
    else:
        return False


@api_blueprint.route('/wanglei/robot', methods=["GET", "POST"])
def wanglei_robot():
    if request.method == 'GET':
        return 'get'
    elif request.method == 'POST':
        req_data = json.loads(request.data.decode())
        post_timestamp = request.headers.get('Timestamp')
        post_sign = request.headers.get('Sign')
        result = check_sign_result(post_timestamp, post_sign)
        if result:
            conversationType = req_data['conversationType']                         # 消息类型，1单聊，2群聊
            conversationId = req_data['conversationId']                             # 加密的会话id
            msgId = req_data['msgId']                                               # 加密的消息id
            senderNick = req_data['senderNick']                                     # 发送消息的人昵称
            isAdmin = req_data['isAdmin']                                           # 是否为管理员
            sessionWebhookExpiredTime = req_data['sessionWebhookExpiredTime']       # 当前会话的Webhook地址过期时间
            createAt = req_data['createAt']                                         # 消息的时间戳
            senderId = req_data['senderId']                                         # 加密的发送者id
            chatbotUserId = req_data['chatbotUserId']                               # 加密的机器人id
            msgtype = req_data['msgtype']                                           # 消息类型，目前只支持text
            text = req_data['text']['content']                                      # 消息的关键字
            sessionWebhook = req_data['sessionWebhook']                             # 当前会话的webhook地址
            robotCode = req_data['robotCode']                                       # 消息机器人代码

            if conversationType == '1':
                # 单聊
                chatbotCorpId = req_data['chatbotCorpId']                           # 加密的机器人所在的企业corpId
                senderStaffId = req_data['senderStaffId']                           # 企业内部群中@该机器人的成员userid
                senderCorpId = req_data['senderCorpId']                             # 企业内部群有的发送者当前群的企业corpId。
                msg = {
                    "text": {
                        "content": "单聊: {}".format(text)
                    },
                    "msgtype": "text"
                }
                return json.dumps(msg)
            else:
                # 群聊
                atUsers = req_data['atUsers']                                       # 被@人的信息
                conversationTitle = req_data['conversationTitle']                   # 群聊时的群名称
                isInAtList = req_data['isInAtList']                                 # 是否在@列表中

                # 如果回复的消息需要@用户，则通过senderNick获取userid，在atUserIds中列出userid即可
                msg = {
                    "at": {
                        "atUserIds": [
                            'manager8575'
                        ],
                        "isAtAll": False
                    },
                    "text": {
                        "content": '群聊: {}'.format(text)
                    },
                    "msgtype": "text"
                }
                return json.dumps(msg)

