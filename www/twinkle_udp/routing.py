from channels.routing import route
from channels.routing import include

from twinkle_udp import consumers

http_routing = [
]

stream_routing = [

]

channel_routing = [
  include(stream_routing),
  include(http_routing),
]
