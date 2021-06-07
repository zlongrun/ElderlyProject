#from django.urls import path
#from chat.consumers import ChatConsumer

#websocket_urlpatterns = [
#    path('ws/chat/', ChatConsumer),
#]
from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/',consumers.ChatConsumer)
]
