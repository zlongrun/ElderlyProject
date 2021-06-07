from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #async_to_sync(self.channel_layer.group_add)(
        #    self.channel_name
        #)
        self.accept()
        self.send({
            "type": "websocket.accept",
        })

    def disconnect(self, close_code):
        #async_to_sync(self.channel_layer.group_discard)(
        #    self.channel_name
        #)
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = '用户：' + text_data_json.get("message", None)
        #response_message = '请输入`help`获取命令帮助信息。'
        self.send({
            "type": "chat_message",
            "message": message,
        })
    
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
