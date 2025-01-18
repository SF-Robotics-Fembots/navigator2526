import socket
import requests
import RPi.GPIO as GPIO
import time

host_ip = '10.0.0.97' 
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host_ip, port))
    s.sendall(b"hello, world")
    data = s.recv(1024)

print(f"received{data!r}")

#setup gpio
GPIO.setmode(GPIO.BCM)
PWM_PIN = 18
GPIO.setup(PWM_PIN, GPIO.OUT)

#initialize pwm
pwm = GPIO.PWM(PWM_PIN, 100)
pwm.start(0)

def get_pwm_value_from_server(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("pwm_value", 0)
    except requests.RequestsException as e:
        print(f"Error fetching pwm values")
        return 0

def main():
    server_url = ""
    try:
        while True:
            pwm_value = get_pwm_value_from_server(server_url)
            duty_cycle = pwm_value / 255*100 #fix this math (not 255 because that's what's its converting from)
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()

            

