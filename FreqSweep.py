import board
import busio
import time
import adafruit_pca9685


def ms_to_duty(freq_hz, pulse_ms):
    period_ms = 1000.0 / freq_hz
    return int((pulse_ms / period_ms) * 65535)


def set_pulse(channel, freq, pulse_ms):
    channel.duty_cycle = ms_to_duty(freq, pulse_ms)


def main():
    thruster_index = int(input("Thruster (1-5): ")) - 1

    ARM_PULSE = 2.2
    NEUTRAL_PULSE = 1.5

    i2c = busio.I2C(board.SCL, board.SDA)
    shield = adafruit_pca9685.PCA9685(i2c)

    thrusterChannels = [
        shield.channels[0],
        shield.channels[1],
        shield.channels[13],
        shield.channels[14],
        shield.channels[15],
    ]

    ch = thrusterChannels[thruster_index]

    print("\nSweeping 90–105 Hz...\n")

    for freq in range(90, 106):  # 90 to 105 inclusive

        print(f"Setting frequency: {freq} Hz")
        shield.frequency = freq
        time.sleep(0.5)  # allow oscillator to settle

        print("  -> ARMING")
        set_pulse(ch, freq, ARM_PULSE)
        time.sleep(2.0)  # listen for ESC beeps

        print("  -> NEUTRAL")
        set_pulse(ch, freq, NEUTRAL_PULSE)
        time.sleep(1.5)

    print("\nSweep complete. Returning to neutral.")
    set_pulse(ch, shield.frequency, NEUTRAL_PULSE)


if __name__ == "__main__":
    main()