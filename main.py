import pygame
import socket
import time, json
#this code actually works so far (convert joystick values to pwm)
#this code works (sending and recieving messages back and forth)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print ("Socket successfully created")


host_ip = '10.0.0.8' 
port = 8080

s.bind((host_ip, port))
s.listen(1)
client_socket, client_address = s.accept()
print ("Socket successfully connected")

try:
    pygame.init()
    print("...")
except:
    print("Canceled")
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
print(joystick_count)
if joystick_count == 0:
    print("No joystick connected")

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick name: {joystick.get_name()}")


def joystick_to_pwm(value):
    pwm_value = 1500 + (value * 500) #1000-2000
    pwm_value = max(1000, min(2000, pwm_value))
    return int(pwm_value)

#*50 or *100 then scale it after
#if dont get value for 0 move according to that

running = True
while running:
    for event in pygame.event.get():
        print(event)
        print("...")
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            axis_0 = joystick.get_axis(0)
            axis_1 = joystick.get_axis(1)
            axis_2 = joystick.get_axis(2)
            axis_3 = joystick.get_axis(3)

            axis_0_rotation = int((axis_0)*100) 
            axis_1_rotation = int((axis_1)*100)
            axis_2_rotation = int((axis_2)*100)
            axis_3_rotation = int((axis_3)*100)

            # joystick_values = [axis_0, axis_1, axis_2, axis_3]

            # thruster_1 = 1
            # thruster_2 = 2
            # thruster_3 = 3
            # thruster_4 = 4
            # thruster_5 = 5

            # thrusters = [thruster_1, thruster_2, thruster_3, thruster_4, thruster_5]

            # rotation = 100/thrusters

            # thruster_1_new = rotation * thruster_1
            # thruster_2_new = rotation * thruster_2

            # thrusters_percent_ideal = [thruster_1, thruster_2, thruster_3, thruster_4, thruster_5]

            # thruster_1_b = 1
            # thruster_2_b = 2
            # thruster_3_b = 3
            # thruster_4_b = 4
            # thruster_5_b = 5

            # thrusters_max_percent = [thruster_1_b, thruster_2_b, thruster_3_b, thruster_4_b, thruster_5_b]

            # abs(thruster_1_b)
            # abs(thruster_2_b)
            # abs(thruster_3_b)
            # abs(thruster_4_b)
            # abs(thruster_5_b)

            # added_values = int(axis_0_rotation + axis_2_rotation)
            # print("x and r:", added_values)

            # if int(added_values > 100 or added_values < 0):
            #     power_limit = int(added_values/(added_values/100))
            #     power_limit = max(100, min(-100, power_limit))
            #     print(power_limit)
            # elif int(added_values < 100):
            #     print(added_values)
            # elif int(added_values = 100):
            #     print(added_values)
            # else:
            #     print("Something went wrong")

            axis_0_pwm_value = joystick_to_pwm(axis_0)
            axis_1_pwm_value = joystick_to_pwm(axis_1)
            axis_2_pwm_value = joystick_to_pwm(axis_2)
            axis_3_pwm_value = joystick_to_pwm(axis_3)

            print(f"Raw Values: Axis 0: {axis_0}, Axis 1: {axis_1}, Axis 2:{axis_2}, Axis 3: {axis_3}")
            print(f"PWM Values: Axis 0: {axis_0_pwm_value}, Axis 1: {axis_1_pwm_value}, Axis 2: {axis_2_pwm_value}, Axis 3: {axis_3_pwm_value}")

            pwm_values = {
                'x': axis_0_pwm_value,
                'y': axis_1_pwm_value,
                'r': axis_2_pwm_value,
                'v': axis_3_pwm_value
            }

            json_data = json.dumps(pwm_values)
            client_socket.sendall(json_data.encode('utf-8'))

            time.sleep(0.005)


pygame.quit()
client_socket.close()