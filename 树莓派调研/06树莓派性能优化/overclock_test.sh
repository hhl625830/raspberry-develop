#!/bin/bash
clear

#show cpu frequency & temperature
cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq
vcgencmd measure_temp

#quick sysbench to test stability and temperature:
sysbench --test=cpu --cpu-max-prime=50000 --num-threads=4 run

#show cpu frequency again:
cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq

#longer sysbench to test stability and temperature:
sysbench --test=cpu --cpu-max-prime=50000 --num-threads=4 run

#show cpu frequency & temperature:
cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq
vcgencmd measure_temp






