import cv2
import threading
import time
import camera0, camera1, camera2, camera3
cameras= camera0, camera1, camera2, camera3
#    0: front, 1:forward down, 2:rear, 3:down

caps = {
    "front": cv2.VideoCapture(0),
    "forward_down": cv2.VideoCapture(1),
    "rear": cv2.VideoCapture(2),
    "down": cv2.VideoCapture(3),
}
class CameraThread(threading.Thread):
    def __init__(self, cam_id, name, cap):
      super().__init__()
      self.cam_id= cam_id
      self.name= name
      self.cap= cap
      self.frame= None
      self.running= True
    def run(self):
       while self.running:
          ret, frame = self.cap.read()
          if ret:
             self.frame= frame
    def stop(self):
       while self.running:
          ret, frame = self.cap.read()
          if ret:
             self.frame= frame
    
class CameraManager:
    def __init__(self):
       self.frames= {}
       self.caps= {
              "front": cv2.VideoCapture(0),
              "forward_down": cv2.VideoCapture(1),
              "rear": cv2.VideoCapture(2),
              "down": cv2.VideoCapture(3),
       }
       self.running= True
       for name in self.caps:
          t= threading.Thread(target=self._update, args=(name,))
          t.start()
    def _update(self, name):
       cap= self.caps[name]
       while self.running:
          ret, frame = cap.read()
          if ret:
             self.frames[name]= frame
    time.sleep(0.01) #prevents cpu hogging

cameras= [
   CameraThread(0, "front"), 
   CameraThread(1, "forward_down"),
   CameraThread(2, "rear"),
   CameraThread(3, "down") 
]
for cam in cameras:
   cam.start()

try:
   while True:
      for cam in cameras:
         if cam.frame is not None:
            display= cam.frame.copy()
            cv2.putText(
               display,
               cam.name,
               (10,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )
            cv2.imshow(cam.name, display)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break
finally:
   for cam in cameras:
      cam.stop()
cv2.destroyAllWindows()
