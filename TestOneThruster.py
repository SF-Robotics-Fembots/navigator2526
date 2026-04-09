import pygame
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import time

def main():
    pygame.init()

    # -------- USER INPUT --------
    try:
        freq = float(input("Enter PWM frequency (Hz, e.g. 50 or 91): "))
        pulse_ms = float(input("Enter pulse width (ms, e.g. 1.5): "))
        thruster_index = int(input("Select thruster (1-5): ")) - 1
    except:
        print("Invalid input.")
        return

    if not (0 <= thruster_index <= 4):
        print("Thruster must be between 1 and 5.")
        return

    # -------- I2C + PCA9685 SETUP --------
    i2c = busio.I2C(board.SCL, board.SDA)
    shield = adafruit_pca9685.PCA9685(i2c)
    shield.external_clock = True
    shield.frequency = freq  # <-- user-defined frequency

    # Thruster channels
    thrusterChannels = [
        shield.channels[0],   # Thruster 1
        shield.channels[1],   # Thruster 2
        shield.channels[13],  # Thruster 3
        shield.channels[14],  # Thruster 4
        shield.channels[15],  # Thruster 5
    ]

    selected_channel = thrusterChannels[thruster_index]

    # -------- FUNCTION --------
    def set_pulse_ms(channel, pulse_ms):
        # Convert ms to duty cycle (16-bit)
        period_ms = 1000.0 / freq
        duty_cycle = int((pulse_ms / period_ms) * 65535)
        channel.duty_cycle = duty_cycle

    # -------- ARM / INITIALIZE ESC --------
    print("Arming ESC...")
    set_pulse_ms(selected_channel, 2.2)  # max
    time.sleep(1)
    set_pulse_ms(selected_channel, 1.5)  # neutral
    time.sleep(1)

    # -------- TEST LOOP --------
    print(f"\nTesting Thruster {thruster_index + 1}")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            set_pulse_ms(selected_channel, pulse_ms)
            print(f"Running at {pulse_ms} ms")
            time.sleep(2)

            set_pulse_ms(selected_channel, 1.5)  # neutral
            print("Back to neutral (1.5 ms)")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping thruster...")
        set_pulse_ms(selected_channel, 1.5)

if __name__ == "__main__":
    main()