# Twinkle UDP

A raspberry pi webserver communicating over UDP with ESP8266 controlled ws2812b lights. 

Ultimately this project is intended to run off of 5V battery packs, allowing for several hours of unique lighting without any infrastructure (power, network, etc).

# Installation

The server utilizes Django (>1.9) with the channels app (as of this time, channels is not core django). I am using the Christopher Keefer's weblog post [Django Channels: From The Ground Up – Part 1](https://docs.djangoproject.com/en/1.9/intro/tutorial01/#creating-a-project) for initial installation instructions, but below are my own notes on getting this up and running.

Start with a [lite version of Raspian](https://www.raspberrypi.org/downloads/raspbian/), then run the following code to install the necessary packages.

```
sudo apt-get -y -q install python python-dev python-pip python-virtualenv libpq-dev postgresql postgresql-contrib nginx supervisor python-software-properties redis-server
```


