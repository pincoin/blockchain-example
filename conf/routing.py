from channels.auth import AuthMiddlewareStack
from channels.routing import (
    ProtocolTypeRouter, URLRouter
)

import blockchain.routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            blockchain.routing.websocket_urlpatterns
        )
    ),
})
