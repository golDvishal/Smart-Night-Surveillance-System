from machine import Pin
import time

# Set up the PIR sensor, LDR module, Buzzer, and optional LED
pir = Pin(16, Pin.IN)    # PIR sensor connected to GPIO 16
ldr = Pin(22, Pin.IN)    # LDR digital output connected to GPIO 22
buzzer = Pin(18, Pin.OUT) # Buzzer connected to GPIO 18
led = Pin(19, Pin.OUT)    # LED connected to GPIO 19 (optional)

# Function to activate alarm (buzzer and LED)
def alarm_on():
    buzzer.value(1)
    led.value(1)

# Function to deactivate alarm
def alarm_off():
    buzzer.value(0)
    led.value(0)

# Main loop
while True:
    # Check if motion is detected by PIR sensor
    if pir.value() == 1:
        print("Motion detected by PIR sensor!")
        alarm_on()
        time.sleep(5)  # Keep alarm on for 5 seconds
        alarm_off()

    # Check if the laser light is interrupted by checking LDR status
    if ldr.value() == 0:  # Laser light interrupted (LDR detects no light)
        print("Laser beam interrupted!")
        alarm_on()
        time.sleep(5)  # Keep alarm on for 5 seconds
        alarm_off()

    # Reset the alarm after checks
    alarm_off()
    time.sleep(0.5)  # Short delay before next sensor check
