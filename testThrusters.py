import board
import busio
import pwmio
#import RPi.GPIO as GPIO # type: ignore
import adafruit_pca9685 #import PCA9685
from adafruit_servokit import ServoKit
import socket, time, json, sys

#set thrusters on bottomside
thruster_5 = 0 #5
thruster_4 = 0 #4
thruster_3 = 0 #3
thruster_2 = 0 #2
thruster_1 = 0 #1
thrusters = [thruster_5, thruster_4, thruster_3, thruster_2, thruster_1]

i2c = busio.I2C(board.SCL, board.SDA)
print("{i2c}")
listofdev = i2c.scan()
print(listofdev)


#i2c = board.I2C() # uses board.SCL and board.SDA
shield = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)
shield.frequency = 98 #was 100

thrusterChannel5 = shield.channels[14] #left vertical
thrusterChannel4 = shield.channels[11] #right vertical
thrusterChannel3 = shield.channels[8] #middle
thrusterChannel2 = shield.channels[15] #left horizontal
thrusterChannel1 = shield.channels[10] #right horizontal
thrusterChannel5.duty_cycle = 0x2666

LV = input("input thrusterChannel5 speed")

throttle_in = 2200
throttlePW = int(throttle_in/10000*65536)
thrusterChannel5.duty_cycle = throttlePW
time.sleep(0)
print("LV")

throttle_in = 1500
throttlePW = int(throttle_in/10000*65536)
thrusterChannel5.duty_cycle = throttlePW
time.sleep(0)
print("LV")

throttlePW = int((LV/10000*65536)*(98/100))
thrusterChannel5.duty_cycle = throttlePW
time.sleep(0)

RV = input("input thrusterChannel4 speed")

throttle_in = 2200
throttlePW = int(throttle_in/10000*65536)
thrusterChannel4.duty_cycle = throttlePW
time.sleep(0)
print("RV")

throttle_in = 1500
throttlePW = int(throttle_in/10000*65536)
thrusterChannel4.duty_cycle = throttlePW
time.sleep(0)
print("RV")

throttlePW = int((RV/10000*65536)*(98/100))
thrusterChannel4.duty_cycle = throttlePW
time.sleep(0)

M = input("input thrusterChannel3 speed")

throttle_in = 2200
throttlePW = int(throttle_in/10000*65536)
thrusterChannel3.duty_cycle = throttlePW
time.sleep(0 )
print("M")

throttle_in = 1500
throttlePW = int(throttle_in/10000*65536)
thrusterChannel3.duty_cycle = throttlePW
time.sleep(0)
print("M")

throttlePW = int((M/10000*65536)*(98/100))
thrusterChannel3.duty_cycle = throttlePW
time.sleep(0)

LH = input("input thrusterChannel2 speed")

throttle_in = 2200
throttlePW = int(throttle_in/10000*65536)
thrusterChannel2.duty_cycle = throttlePW
time.sleep(0)
print("LH")

throttle_in = 1500
throttlePW = int(throttle_in/10000*65536)
thrusterChannel2.duty_cycle = throttlePW
time.sleep(0)
print("LH")

throttlePW = int((LH/10000*65536)*(98/100))
thrusterChannel2.duty_cycle = throttlePW
time.sleep(0)

RH = input("input thrusterChannel1 speed")

throttle_in = 2200
throttlePW = int(throttle_in/10000*65536)
thrusterChannel1.duty_cycle = throttlePW
time.sleep(0)
print("RH")

throttle_in = 1500
throttlePW = int(throttle_in/10000*65536)
thrusterChannel1.duty_cycle = throttlePW
time.sleep(0)
print("RH")

throttlePW = int((RH/10000*65536)*(98/100))
thrusterChannel1.duty_cycle = throttlePW
time.sleep(0)