# mysite/asgi.py

#import os

#import django
#from channels.http import AsgiHandler
#from channels.routing import ProtocolTypeRouter

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ElderlyProject.settings')
#django.setup()

#application = ProtocolTypeRouter({
#  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
#})

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ElderlyProject.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})