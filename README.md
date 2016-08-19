# Twinkle UDP

A raspberry pi webserver communicating over UDP with ESP8266 controlled ws2812b lights.

Ultimately this project is intended to run off of 5V battery packs, allowing for several hours of unique lighting without any infrastructure (power, network, etc).

# Installation

The server utilizes Django (>1.9) with the channels app (as of this time, channels is not core django). I am using the Christopher Keefer's weblog post [Django Channels: From The Ground Up – Part 1](http://artandlogic.com/2016/06/django-channels-ground-part-1/) for initial installation instructions, but below are my own notes on getting this up and running.

Start with a [lite version of Raspian](https://www.raspberrypi.org/downloads/raspbian/), then run the following command to install the necessary packages and setup the environment:

```bash
# performed as root
sudo add-apt-repository -y ppa:rwky/redis
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python python-pip python-dev python-pip python-virtualenv nginx supervisor python-software-properties redis-server
sudo adduser web
su web
cd ~
mkdir venv
virtualenv --no-site-packages ~/venv
```

Next copy the files:

```bash
# performed as web
git pull https://github.com/stevarino/twinkle_udp
```

If you're using vagrant (hashicorp/precise64 works for me) and you already have the files linked to the /vagrant directory, you can also do the following command will also work:

```bash
# OPTIONAL VAGRANT METHOD - performed as web
ln -s /vagrant/twinkle_udp/ ~/twinkle_udp
```

Now let's get everything running! This script should get everything up and running:

```bash
# performed as root
cd /home/web/twinkle_udp
sudo ./post-receive
```

Now your server should be running.
