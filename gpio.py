import requests


LED_on = True
LED_off = False
counter = 0
response = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

# clear lights and webserver counters
GPIO.output(18, LED_off)
requests.get('http://aws-webserver/reset')
requests.get('http://localhost:9100/reset')

while True:
        if not GPIO.input(25):
                counter += 1
                if counter == 1:
                        print("-><- aws")

                if counter == 2:
                        print("-><- edge(local)")

        if counter == 1:
                #print("-><-  aws")
                requests.get('http://aws-webserver/push?temp=100')
                response = requests.get('http://aws-webserver/get')
                if response.text == "25":
                        GPIO.output(18, LED_on)
                        time.sleep(4)
                        GPIO.output(18, LED_off)

        if counter == 2:
                #print("-><- edge (local)")
                requests.get('http://localhost:9100/push?temp=100')
                response = requests.get('http://localhost:9100/get')
                if response.text == "25":
                        GPIO.output(18, LED_on)

        if counter >= 3:
                print("Test Complete")
                GPIO.output(18, LED_off)
                GPIO.cleanup()
                requests.get('http://aws-webserver/reset')
                requests.get('http://localhost:9100/reset')
                break
