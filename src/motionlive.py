import RPi.GPIO as GPIO
import time
import requests  # Handles the HTTP connection to ThingSpeak

# Use BCM numbering for Raspberry Pi GPIO pins
GPIO.setmode(GPIO.BCM)

# Pin Setup 
PIR_PIN = 4
LED_PIN = 17
BUZZER_PIN = 27 

# ----------------------------------------------------
# THINGSPEAK CLOUD CONFIGURATION
# ----------------------------------------------------
#  Make sure to paste your actual Write API Key between the quotes!
API_KEY = "756GZGCM5LH7XSMS" 
URL = "https://api.thingspeak.com/update"

# Configure hardware pin directions
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT) 

# Force actuators off initially to guarantee a clean state
GPIO.output(LED_PIN, False)
GPIO.output(BUZZER_PIN, False)

print("==================================================")
print("     SDT 2133 IOT SECURITY SYSTEM INITIALIZING    ")
print("==================================================")
print("Warming up PIR sensor... Please wait 20 seconds.")
time.sleep(20)  # Crucial calibration window to prevent false startup alarms
print("System Live! Monitoring for intruder movements...\n")

try:
    while True:
        # Check if the hardware sensor pin reads HIGH (Movement found)
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            print("INTRUDER DETECTED! Triggering alerts...")
            
            # 1. Turn both local hardware actuators ON 
            GPIO.output(LED_PIN, True)
            GPIO.output(BUZZER_PIN, True)
            
            # 2. Transmit '1' to Cloud (Spikes line chart UP, triggers Red Lamp)
            print("Sending alert state '1' to ThingSpeak...")
            try:
                payload = {'api_key': API_KEY, 'field1': 1}
                response = requests.get(URL, params=payload, timeout=5)
                print(f"Alert Uploaded! Server Response Entry ID: {response.text}")
            except Exception as e:
                print(f" Cloud Connection Error: {e}")
            
            # 3. Maintain local hardware alarm for 2 seconds
            time.sleep(2) 
            
            # 4. Turn both local hardware actuators OFF
            GPIO.output(LED_PIN, False)
            GPIO.output(BUZZER_PIN, False)
            print("Local alerts silenced.")
            
            # 5. Rate Limit Protection Cooldown Buffer
            # ThingSpeak drops any data sent less than 15 seconds apart.
            print("Cooling down for 15 seconds to obey cloud server rules...")
            time.sleep(15) 
            
            # 6. Transmit '0' to Cloud (Pulls line chart DOWN, turns Lamp off)
            print("Area clear. Sending reset state '0' to ThingSpeak...")
            try:
                payload = {'api_key': API_KEY, 'field1': 0}
                response = requests.get(URL, params=payload, timeout=5)
                print(f" Reset Uploaded! Server Response Entry ID: {response.text}")
            except Exception as e:
                print(f" Cloud Reset Failed: {e}")
                
            print("\n System reset complete. Scanning for movement...")
        
        # Idle state loop deceleration to keep Pi CPU utilization at ~0%
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[INFO] Security system stopped manually.")

finally:
    # Safely releases the pins so they don't stay energized or throw warnings next run
    GPIO.cleanup()
    print("GPIO cleanup successful. Pins set to safe default states. System offline.")
