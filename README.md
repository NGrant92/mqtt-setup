# Basic MQTT Setup  
### A guide to set up an MQTT broker on a RaspberryPi to allow your devices communicate with eachother  

### Requirements:  
- RaspberryPi:  
  - Docker ([ref](https://www.raspberrypi.org/blog/docker-comes-to-raspberry-pi/))


- Other Devices:
  - Python3 is required to send/recieve messages

### Setup:
Add a credentials file
> touch src/credentials.json

Add the private/public ip of the RaspberryPi like so:  
```json
{
  "broker_address": "x.x.x.x"
}

```
Replace x.x.x.x with iP of Pi

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
