import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False)
#You can import any required modules here

#This can be anything you want
moduleName = "turnON"

#All of the words must be heard in order for this module to be executed
commandWords = ["turn", "on"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
    print("turning the LED ON, It's not magic, Said: Manojkumar")
    GPIO.output(40, GPIO.HIGH)
    return



