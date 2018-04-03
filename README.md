# Basic MQTT Setup  
### A guide to set up an MQTT broker on a RaspberryPi to allow your devices communicate with eachother  

### Requirements:  
- RaspberryPi:  
  - Docker ([ref](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/))


- Other Devices:
  - Python3 is required to send/recieve messages

### Setup:
**RaspberryPi:**  

Download MQTT docker image suited to run on RaspberryPi  
> docker pull pascaldevink/rpi-mosquitto:latest  

Boot up the container  
> ./dockerrun.sh  

**Device:**  
Copy files from `src` folder to devices  

`pub_to.py`  
- publishes to a currently hardcoded channel "mac"  
- command: `python3 pub_to.py message`

`sub_to.py`  
- subscribes to currently hardcoded channel "mac"  
- command: `python3 sub_to.py`
- cancel: `ctrl+c`
