# TODO: uncomment everything
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT

mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!


def turnOffMotors():
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


atexit.register(turnOffMotors)

#################################

leftMotor = mh.getMotor(3)
rightMotor = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
leftMotor.setSpeed(150)
leftMotor.run(Adafruit_MotorHAT.FORWARD)
rightMotor.setSpeed(150)
rightMotor.run(Adafruit_MotorHAT.FORWARD)
# turn on motor
leftMotor.run(Adafruit_MotorHAT.RELEASE)
rightMotor.run(Adafruit_MotorHAT.RELEASE)


def move_rover(direction):
    if direction == 'forward':
        leftMotor.run(Adafruit_MotorHAT.FORWARD)
        rightMotor.run(Adafruit_MotorHAT.FORWARD)
    elif direction == 'backward':
        leftMotor.run(Adafruit_MotorHAT.BACKWARD)
        rightMotor.run(Adafruit_MotorHAT.BACKWARD)
    elif direction == 'right':
        leftMotor.run(Adafruit_MotorHAT.RELEASE)
        rightMotor.run(Adafruit_MotorHAT.FORWARD)
    elif direction == 'left':
        leftMotor.run(Adafruit_MotorHAT.FORWARD)
        rightMotor.run(Adafruit_MotorHAT.RELEASE)


def stop_rover():
    leftMotor.run(Adafruit_MotorHAT.RELEASE)
    rightMotor.run(Adafruit_MotorHAT.RELEASE)
