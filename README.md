temperature
===========

Measuring temperature with DS18B20 on Raspberry pi and display measured data.

Here is sources which I used:

1) Reading temperature from DS18B20 - Read temperature from thermometer, then the value save to the temp.log .      

2) Displaying measured data - js library, read file temp.log, and display measured data in graph.

https://github.com/danvk/dygraphs


3) Cron daemon in linux run the python code every minute (Read temperature from thermometer, then the value save to the temp.log).


pi@raspberrypi ~/temperature $ crontab -e

To the bottom of the file add this line.

*/1  *    * * *   pi      python /home/pi/temperature/temperature.py

