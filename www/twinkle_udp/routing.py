from channels.routing import route
from channels.routing import include
 
from twinkle_udp import consumers
 
http_routing = [
  route('http.request', consumers.http_consumer)
]
 
stream_routing = [
 
]
 
channel_routing = [
  include(stream_routing),
  include(http_routing),
]
