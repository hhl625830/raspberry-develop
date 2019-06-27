import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
import urllib.request
#while True:
 #   GPIO.output(38, GPIO.HIGH)
  #  time.sleep(1)
   # GPIO.output(38, GPIO.LOW)
    #time.sleep(1)
    
def check_network():
    while True:
        try:
            result = urllib.request.urlopen('http://baidu.com').read()
            print(type(result))
            print(result)
            print("Network is Ready!")
            GPIO.output(38, GPIO.LOW)
            break
        except Exception as e:
            GPIO.output(38, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(38, GPIO.LOW)
            print(e)
            print("Network is not ready,Sleep 5s...")
            time.sleep(1)
        
        
    return True


if __name__ == '__main__':
    check_network()
    
    