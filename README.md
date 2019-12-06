# raspi-monitor-sleep
turns off raspberry pi monitor based on GPIO input

useful for magic mirrors since the existing libraries are not great

### setup:
* `chmod +x turnon.sh`
* `chmod +x turnoff.sh`
* set to run at boot: `python /home/pi/raspi-monitor-sleep/watcher.py

portions of the code were lifted from elsewhere but i can't remember where
