import RPi.GPIO as GPIO
import time
import subprocess
        
GPIO.setmode(GPIO.BCM)

# The GPIO's that are currently used
TRIG = 23
ECHO = 24

# Sets display power on, to be sure that standard variable is defined 
power = 1 
bashCommand = "vcgencmd display_power 1"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

# The moment when distance has changed
time_last_hit = time.time()

# To be sure that the distance has really changed, if sensor is not always accurate
last_measurement = 0


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# The measurment for the distance (Function)
def measurement():
  global last_measurement

  GPIO.output(TRIG, False)
  time.sleep(0.1) 
  
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

# Calculates the distance to Cm (Centimeters)
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150

  distance = round(distance, 2)

  # If the distance changes to under 125 Cm, say yes
  if distance < 125 and last_measurement < 125:
      last_measurement = distance
      return True
  # Otherwise (so if it does not changes under 125 Cm), say no
  else:
      last_measurement = distance
      return False

# main program loop
while True:
    Is_somebody_close = measurement()
    if Is_somebody_close == True:
        if power == 0:
          bashCommand = "vcgencmd display_power 1"
          process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        print "hit timestamp (sec since 1-1-1970): "+str(time.time())
        time_last_hit = time.time()
        power = 1

    if Is_somebody_close == False and (time.time() - time_last_hit > 7200) and power == 1:
        bashCommand = "vcgencmd display_power 0"        
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        print "turned off power to screen"
        power = 0





