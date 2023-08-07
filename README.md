# cpu-stresstest
I created a Simple CPU stress test to test my Raspberry Pi's stability. For any questions, feel free to contact me at tomas.hermansky@gmail.com. 

You can specify the duration of the stress test when you run the script with the -d or --duration option, like so:

python stresstest.py --duration 120

This would run the stress test for 120 seconds. If you don't specify a duration, it defaults to 60 seconds.

Please note this script is very basic and the primary purpose is to test the temperature and behavior of computers like Raspberry PI under stress - the output (CPU load before/after stress test) is not very accurate.
