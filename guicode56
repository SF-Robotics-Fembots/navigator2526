import pygame
from logging import root
from socket import socket
import tkinter as tk

# Initialize Pygame and Joystick

m = tk.Tk()
self= m
m.title("ROV Control Interface")
#widgets added here, such as camera display, thruster status, etc.
joystick_count= pygame.joystick.get_count() #connection
print(joystick_count)
if joystick_count == 0:
    from tkinter import *
    main = Tk()
    ourMessage = 'no joystick connected'
    messageVar = Message(main, text=ourMessage)
    messageVar.config(bg='lightpink', font=('times', 24, 'italic'))
    messageVar.pack()
    self.status_label= tk.Label(m, text="joystick disconnected")

else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("joystick connected")
    print("joystick name: {joystick.get_name()}")
class Joystick:
    host_ip= '' #'
    port= '' #replace both
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host_ip,port)) #insert host ip
    s.listen(1)
    client_socket, client_address= s.accept() #connecting the socket
    print("socket connected") 
    '''probably dont need the socket because 
    emily may have it in her code'''

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def read(self):
        pygame.event.pump()
        return {
            "forward_backward":  -self.joystick.get_axis(1),
            "yaw": self.joystick.get_axis(0),
            "vertical": -self.joystick.get_axis(3),
            "arm": self.joystick.get_button(0),
        }
    def apply_deadzone(self,value, deadzone= 0.1):
        return 0 if abs(value) < deadzone else value
    def update_joystick(self):
        pygame.event.pump()
        self.forward_backward = self.apply_deadzone(-self.joystick.get_axis(1))
        self.yaw = self.apply_deadzone(self.joystick.get_axis(0))
        self.vertical = self.apply_deadzone(-self.joystick.get_axis(3))
        self.arm = self.joystick.get_button(0)

    def emergency_stop(self):
        print("Emergency stop activated")
    try:
        axis= self.joystick.get_axis(0)
    except pygame.error:
        self.connected = False

m.mainloop()
self.connected = True

socket.close()
root.quit()
root.destroy()
