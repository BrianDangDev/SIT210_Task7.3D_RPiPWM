import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 16  
GPIO_GPIO_ECHO = 18
LED = 12  
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_GPIO_ECHO,GPIO.IN)  
GPIO.setup(LED,GPIO.OUT)  
 
GPIO.output(GPIO_TRIGGER, False)
LEDPWM = GPIO.PWM(LED, 100)  
LEDPWM.start(0);  
try:
    while True:
        GPIO.output(GPIO_TRIGGER, True)  
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
       
        #set the beggining of the time
        while GPIO.input(GPIO_GPIO_ECHO)==0:
            StartTime = time.time()
        #set the Ending of the time
        while GPIO.input(GPIO_GPIO_ECHO)==1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
       
        distance = (TimeElapsed * 34000) / 2  
        print ("distance:",distance,"cm")  
        if distance<=50:  
            for x in range(50,101,10):  
                LEDPWM.ChangeDutyCycle(x)  
                time.sleep(0.1)  
               
        elif distance>50:  
            for x in range(50,-1,-10):   
                LEDPWM.ChangeDutyCycle(x)  
                time.sleep(0.2) 
except KeyboardInterrupt:
    LEDPWM.stop()
    GPIO.cleanup()