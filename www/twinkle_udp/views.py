from django.shortcuts import render

import socket
import struct
import sys
import time


def index(request):
    try:
        id = request.POST['id']
    except KeyError:
        pass
    else:
        command = request.POST['command']
        color1 = request.POST['color1']
        color2 = request.POST['color2']
        timing = request.POST['delay']
        count = request.POST['count']

        if command == '01':
            send_command(id+command+color1)
        elif command == '02':
            send_command(id+command+timing)
        elif command == '03':
            send_command(id+cocmmand+color1+color2+count+timing)
        elif command == 'FE':
            send_command(id+comand+count)
        else:
            send_command(id+command)

    return render(request, 'twinkle_udp/templates/index.html')

def send_command(message):
    send_udp(message)
    time.sleep(0.01)
    send_udp(message)
    time.sleep(0.01)
    send_udp(message)
    
def send_udp(message):
    message = message.decode("hex")
    # multicast_group = ("228.239.239.239", 32440)
    multicast_group = ("192.168.1.255", 32440)

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(1)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    try:
        # Send data to the multicast group
        print >>sys.stderr, 'sending "%s"' % message
        sent = sock.sendto(message, multicast_group)

        # Look for responses from all recipients
        # while True:
        #     print >>sys.stderr, 'waiting to receive'
        #     try:
        #         data, server = sock.recvfrom(16)
        #     except socket.timeout:
        #         print >>sys.stderr, 'timed out, no more responses'
        #         break
        #     else:
        #         print >>sys.stderr, 'received "%s" from %s' % (data, server)

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
